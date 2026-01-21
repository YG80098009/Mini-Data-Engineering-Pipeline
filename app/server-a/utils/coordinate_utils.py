


class CoordinatesUtils:

    @staticmethod
    def filter_data(data):
        result = data["results"][0]
        return {
            "location_name": result["name"],
            "country": result.get("country"),
            "latitude": result["latitude"],
            "longitude": result["longitude"]
        }
    @staticmethod
    def check_data(data: dict) -> bool:
        if "results" not in data or not data["results"]:
            return False 
        return True
    
    @staticmethod    
    def raise_error(location_name: str):
        raise ValueError(f"Location not found: {location_name}")