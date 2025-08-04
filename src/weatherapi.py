import os
from dotenv import load_dotenv
import requests

load_dotenv()

def fetch_weather(city: str) -> str:
    api_key = os.getenv("OPENWEATHER_API")
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    resp = requests.get(url).json()
    
    if resp.get("cod") != 200:
        return f"Could not fetch weather for {city}. Error: {resp.get('message')}"
    
    desc = resp["weather"][0]["description"]
    temp = resp["main"]["temp"]
    return f"Weather in {city}: {desc}, {temp}°C"
