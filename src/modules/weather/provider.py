from abc import ABC, abstractmethod


class BaseWeatherProvider(ABC):
    """Abstract interface for weather data providers."""

    @abstractmethod
    def fetch_weather(self, latitude, longitude):
        """Fetch current weather for given coordinates.

        Returns a dict with standardized keys:
            - temperature (float): Temperature in °C
            - description (str): Human-readable weather description
            - wind_speed (float): Wind speed in km/h
        """
        ...
