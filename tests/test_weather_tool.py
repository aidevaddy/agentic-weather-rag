import os
from tools.weather import get_current_weather

def test_weather_tool_no_api_key(monkeypatch):
    # Mocking no API key in environment
    monkeypatch.delenv("OPENWEATHER_API_KEY",raising=False)

    result=get_current_weather.invoke({"city":"Nashik"})

    assert "error" in result
    assert "API key" in result["error"]