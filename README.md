# temperature logging 

A Python script that tracks daily temperature data (current, minimum, and maximum) for multiple cities using the Open-Meteo API. The script stores the data in a CSV file and can be automated to run daily.

## Features

- Tracks temperatures for Bangalore, Hyderabad, Barcelona, Antwerp, and Santa Clara
- Records current, minimum, and maximum temperatures in Celsius
- Stores data in a CSV file for historical tracking
- No API key required
- Automatic timezone handling
- Error handling and logging

## Requirements

- Python 3.6 or higher
- Required Python packages:
  - requests
  - pandas

## Usage

### Running the Script Manually

```bash
python temperature_tracker.py
```

### Output

The script creates a CSV file named `temperature_records.csv` with the following columns:
- Date
- City
- Current_Temp
- Min_Temp
- Max_Temp

The script also displays the latest temperature records in the console when run.

### Automating the Script

#### Windows

1. Create a batch file (run_tracker.bat):
```batch
@echo off
python path/to/your/temperature_tracker.py
```

2. Open Task Scheduler:
   - Create a new Basic Task
   - Set trigger to run daily
   - Action: Start a program
   - Program/script: path to your batch file

#### Linux/Mac

Add to crontab to run daily at midnight:
```bash
0 0 * * * /usr/bin/python3 /path/to/your/temperature_tracker.py
```

## Data Source

This script uses the [Open-Meteo API](https://open-meteo.com/), which provides:
- Free weather data
- No API key required
- High reliability
- Accurate temperature measurements

## City Coordinates

The script tracks the following cities with their coordinates:
- Bangalore: 12.9716°N, 77.5946°E
- Hyderabad: 17.3850°N, 78.4867°E
- Barcelona: 41.3851°N, 2.1734°E
- Antwerp: 51.2194°N, 4.4025°E
- Santa Clara: 37.3541°N, -121.9552°W

## Customization

To add or modify cities, edit the `cities` dictionary in the `WeatherTracker` class:

```python
self.cities = {
    'New_City_Name': {'lat': latitude, 'lon': longitude}
}
```
