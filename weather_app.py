import requests
from datetime import datetime
from colorama import Fore, init

# Initialize
init(autoreset=True)

API_KEY = "dda9218de1e47e602202378f638fe952".strip()
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

# Input the cities 
cities = ["Mumbai", "Delhi", "Bangalore", "Kolkata", "Chennai"]

for city in cities:
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }

    response = requests.get(BASE_URL, params=params)
    data = response.json()

    if data.get("cod") != 200:
        print(Fore.RED + f"Error fetching data for {city}: {data.get('message')}")
        continue

    # Data Extraction
    location = f"{data['name']}, {data['sys']['country']}"
    current_time = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    weather = data["weather"][0]["description"].title()
    temperature = data["main"]["temp"]
    feels_like = data["main"]["feels_like"]
    humidity = data["main"]["humidity"]
    wind_speed = data["wind"]["speed"]

    # Print
    print(Fore.CYAN + "\n================ Weather Report ================")
    print(Fore.YELLOW + f"Location: {location}")
    print(Fore.GREEN + f"Date & Time: {current_time}")
    print(Fore.MAGENTA + f"Weather: {weather}")
    print(Fore.BLUE + f"Temperature: {temperature}°C (Feels like: {feels_like}°C)")
    print(Fore.CYAN + f"Humidity: {humidity}%")
    print(Fore.RED + f"Wind Speed: {wind_speed} m/s")
    print(Fore.CYAN + "================================================")

