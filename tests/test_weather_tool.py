import os
import requests
from _pytest.monkeypatch import MonkeyPatch
from tools.weather import get_current_weather
from tools.weather import _get_current_weather


def test_weather_tool_no_api_key(monkeypatch: MonkeyPatch):
    # Mocking no API key in environment
    monkeypatch.delenv("OPENWEATHER_API_KEY",raising=False)

    result=get_current_weather.invoke({"city":"Nashik"})

    assert "error" in result
    assert "API key" in result["error"]

def test_weather_tool_returns_dict(monkeypatch):
    result = _get_current_weather("Chennai")

    assert isinstance(result, dict)
    assert "city" in result or "error" in result