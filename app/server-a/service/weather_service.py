import requests 
from typing import Any 

class WheatherService:
    @staticmethod
    def send_coordinate(latitude: float, longitude: float):
        """send the lat and lon and ruturn params"""
        params = {
            "latitude": latitude,
            "longitude": longitude,
            "hourly": "temperature_2m,wind_speed_10m,relative_humidity_2m",
            "past_days": 1,
            "timezone": "UTC"
        }
        return params
    
    @staticmethod
    def fetch_hourly_weather(latitude: float, longitude: float) -> dict:
        """get the params and return """
        url = "https://api.open-meteo.com/v1/forecast"
        params = WheatherService.send_coordinate(latitude, longitude)
        response = requests.get(url, params=params)
        response.raise_for_status()
        data: dict = response.json()["hourly"]
        return data



