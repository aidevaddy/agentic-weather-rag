import os
import requests
from langchain.tools import tool

@tool
def get_current_weather(city: str)->dict:
    """
    Fetch weather for a current city using OpenWeatherMap API

    Args:
    city: The city for which weather needs to be fetched
    """
    weather_api_key=os.environ.get("OPENWEATHER_API_KEY",None)
    if not weather_api_key:
        return {"error":"OPEN Weather API key not set"}