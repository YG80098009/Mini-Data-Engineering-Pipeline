import requests 
from typing import Any


class CoordinatesService:
    # will come from the env file
    @staticmethod
    def location(location_name: str):
        """create params based on the location name"""
        params: dict[str,Any] = {
            "name": location_name,
            "count": 1
        } 
        return params
    @staticmethod
    def fetch_coordinates(params: dict[str,Any]) -> dict:
        """send request to the site and return the data"""
        url = "https://geocoding-api.open-meteo.com/v1/search"
        response = requests.get(url, params=params)
        response.raise_for_status()
        data: dict = response.json()
        return data

