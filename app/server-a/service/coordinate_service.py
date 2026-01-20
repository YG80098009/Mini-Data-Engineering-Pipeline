import requests 
from typing import Any, Dict

url = "https://geocoding-api.open-meteo.com/v1/search" 
class CoordinatesService:
    # will come from the env file
    def location(self, location_name: str):
        """create params based on the location name"""
        params: dict[str,Any] = {
            "name": location_name,
            "count": 1
        } 
        return params

    def fetch_coordinates(self, url: str, params: dict[str,Any]) -> dict:
        """send request to the site and return the data"""
        response = requests.get(url, params=params)
        response.raise_for_status()
        data: dict = response.json()
        return data

    def filter_data(self, data):
        result = data["results"][0]
        return {
            "location_name": result["name"],
            "country": result.get("country"),
            "latitude": result["latitude"],
            "longitude": result["longitude"]
        }
    
    def check_data(self, data):
        if "results" not in data or not data["results"]:
            return False 
        
    def raise_error(self, location_name):
        raise ValueError(f"Location not found: {location_name}")