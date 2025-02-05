import requests
import pandas as pd
from datetime import datetime
import os
from typing import Dict, Optional


class WeatherTracker:
    def __init__(self):
        self.cities = {
            'Bangalore': {'lat': 12.9716, 'lon': 77.5946},
            'Hyderabad': {'lat': 17.3850, 'lon': 78.4867},
            'Barcelona': {'lat': 41.3851, 'lon': 2.1734},
            'Antwerp': {'lat': 51.2194, 'lon': 4.4025},
            'Santa Clara': {'lat': 37.3541, 'lon': -121.9552}
        }
        self.output_file = 'temperature_records.csv'

    def get_temperature_data(self, city: str, coords: Dict[str, float]) -> Optional[Dict[str, float]]:
        """
        Fetch temperature data from Open-Meteo API
        Returns current, min and max temperatures in Celsius
        """
        url = (
            f"https://api.open-meteo.com/v1/forecast?"
            f"latitude={coords['lat']}&longitude={coords['lon']}"
            f"&current=temperature_2m"
            f"&daily=temperature_2m_max,temperature_2m_min"
            f"&timezone=auto"
        )

        try:
            response = requests.get(url)
            response.raise_for_status()
            data = response.json()

            return {
                'current': round(data['current']['temperature_2m'], 1),
                'min': round(data['daily']['temperature_2m_min'][0], 1),
                'max': round(data['daily']['temperature_2m_max'][0], 1)
            }

        except Exception as e:
            print(f"Error fetching data for {city}: {str(e)}")
            return None

    def record_temperatures(self):
        """
        Record daily temperatures for all cities and save to CSV
        """
        today = datetime.now().strftime('%Y-%m-%d')
        records = []

        for city, coords in self.cities.items():
            temp_data = self.get_temperature_data(city, coords)

            if temp_data:
                records.append({
                    'Date': today,
                    'City': city,
                    'Current_Temp': temp_data['current'],
                    'Min_Temp': temp_data['min'],
                    'Max_Temp': temp_data['max']
                })
                print(f"Retrieved temperatures for {city}")
            else:
                print(f"Failed to retrieve temperatures for {city}")

        # Create or update CSV file
        if records:
            df = pd.DataFrame(records)

            if os.path.exists(self.output_file):
                existing_df = pd.read_csv(self.output_file)
                df = pd.concat([existing_df, df], ignore_index=True)

            df.to_csv(self.output_file, index=False)
            print(f"\nTemperature records updated for {today}")
        else:
            print("No data was collected")

    def display_latest_records(self):
        """
        Display the latest temperature records for all cities
        """
        if os.path.exists(self.output_file):
            df = pd.read_csv(self.output_file)
            latest_date = df['Date'].max()
            latest_records = df[df['Date'] == latest_date]

            print(f"\nLatest Temperature Records ({latest_date}):")
            print("=" * 70)
            for _, row in latest_records.iterrows():
                print(f"{row['City']}:")
                print(f"  Current: {row['Current_Temp']:.1f}°C")
                print(f"  Min: {row['Min_Temp']:.1f}°C")
                print(f"  Max: {row['Max_Temp']:.1f}°C")
                print("-" * 30)


if __name__ == "__main__":
    tracker = WeatherTracker()
    tracker.record_temperatures()
    tracker.display_latest_records()