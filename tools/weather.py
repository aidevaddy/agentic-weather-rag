import os
import requests
from langchain.tools import tool
from pydantic import BaseModel

class WeatherResult(BaseModel):
    city: str
    temperature: float
    unit: str
    description: str

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
    
    url = os.environ.get("OPENWEATHER_API_URL",None)
    if not url:
        return {"error":"OPEN Weather API url not set"}
    params = {
        "q":city,
        "appid":weather_api_key,
        "units":"metric"
    }

    response = requests.get(url,params=params,timeout=10)

    if response.status_code!=200:
        return {
            "error":f"Weather API error: {response.status_code}",
            "details": response.text
        }
    
    data = response.json()

    result = WeatherResult(
        city=data.get("name"),
        temperature=data.get("main", {}).get("temp"),
        unit="celsius",
        description=data.get("weather", [{}])[0].get("description"),
    )

    return result.model_dump()

print(get_current_weather.invoke({"city": "London"}))