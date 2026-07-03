import requests

from src.modules.weather.provider import BaseWeatherProvider


# WMO Weather Interpretation Codes (WW)
# https://open-meteo.com/en/docs
WMO_CODES = {
    0: "Clear sky",
    1: "Mainly clear",
    2: "Partly cloudy",
    3: "Overcast",
    45: "Fog",
    48: "Depositing rime fog",
    51: "Light drizzle",
    53: "Moderate drizzle",
    55: "Dense drizzle",
    56: "Light freezing drizzle",
    57: "Dense freezing drizzle",
    61: "Slight rain",
    63: "Moderate rain",
    65: "Heavy rain",
    66: "Light freezing rain",
    67: "Heavy freezing rain",
    71: "Slight snowfall",
    73: "Moderate snowfall",
    75: "Heavy snowfall",
    77: "Snow grains",
    80: "Slight rain showers",
    81: "Moderate rain showers",
    82: "Violent rain showers",
    85: "Slight snow showers",
    86: "Heavy snow showers",
    95: "Thunderstorm",
    96: "Thunderstorm with slight hail",
    99: "Thunderstorm with heavy hail",
}


class OpenMeteoProvider(BaseWeatherProvider):
    """Weather provider using the Open-Meteo API (no API key required)."""

    BASE_URL = "https://api.open-meteo.com/v1/forecast"

    def fetch_weather(self, latitude, longitude):
        params = {
            "latitude": latitude,
            "longitude": longitude,
            "current": "temperature_2m,weather_code,wind_speed_10m",
        }

        r = requests.get(self.BASE_URL, params=params, timeout=10)
        r.raise_for_status()

        current = r.json()["current"]

        weather_code = current["weather_code"]

        return {
            "temperature": current["temperature_2m"],
            "description": WMO_CODES.get(weather_code, "Unknown"),
            "wind_speed": current["wind_speed_10m"],
        }
