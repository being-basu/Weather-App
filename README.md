# Weather App

A simple Python command-line application that fetches live weather data for multiple Indian cities using the OpenWeatherMap API.

## Features

- Retrieves temperature, humidity, weather condition, wind speed.
- Colored terminal output using Colorama for better readability.
- Handles errors if city data is not found.

## API Key Setup

1. Sign up for a free account at OpenWeatherMap (https://openweathermap.org/api).  
2. Generate your own API key from their dashboard.  
3. Replace the API_KEY variable in weather.py with your API key string.  
4. Without a valid API key, the script won’t fetch weather data.

Note: The script currently contains an API key, but for security, you might want to replace it with your own key.

## How to Run

1. Make sure Python 3 is installed on your system.

2. Install required libraries:
```
pip install requests colorama
```
3. Run the script:
```
python weather.py
```

## Example Output

================ Weather Report ================  <br>
Location: Mumbai, IN  <br>
Date & Time: 12-08-2025 15:30:45  <br>
Weather: Clear Sky 
Temperature: 32°C (Feels like: 34°C)  <br>
Humidity: 70%  <br>
Wind Speed: 5 m/s <br>



Basu
