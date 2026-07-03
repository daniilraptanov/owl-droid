from src.modules.base import BaseModule
from src.modules.weather.provider import BaseWeatherProvider


class WeatherContextModule(BaseModule):
    """Provides current weather context using a pluggable weather provider."""

    def __init__(self, provider, latitude, longitude):
        if not isinstance(provider, BaseWeatherProvider):
            raise TypeError("provider must be an instance of BaseWeatherProvider")

        self.provider = provider
        self.latitude = latitude
        self.longitude = longitude

    def get_context(self):
        data = self.provider.fetch_weather(self.latitude, self.longitude)

        return {
            "temperature": data["temperature"],
            "weather": data["description"],
            "wind_speed": data["wind_speed"],
        }

    def get_prompt_section(self, ctx):
        return (
            f"Weather: {ctx['weather']}, {ctx['temperature']}°C, "
            f"wind {ctx['wind_speed']} km/h"
        )
