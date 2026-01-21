from datetime import datetime
from .coordinate_service import CoordinatesService
from .weather_service import WheatherService
from utils.coordinate_utils import CoordinatesUtils
from dotenv import load_dotenv
import os 


class Ingest:
    records = []
    load_dotenv()
    coor_url = os.getenv("coor_url")

    @staticmethod
    def ingest_weather_for_location(location_name):
        param = CoordinatesService.location(location_name)
        location = CoordinatesService.fetch_coordinates(param)
        
        if not CoordinatesUtils.check_data(location):
            CoordinatesUtils.raise_error(location_name)
        location = CoordinatesUtils.filter_data(location)

        hourly_data = WheatherService.fetch_hourly_weather(
            location["latitude"],
            location["longitude"]
        )

        times = hourly_data["time"]
        temperatures = hourly_data["temperature_2m"]
        wind_speeds = hourly_data["wind_speed_10m"]
        humidities = hourly_data["relative_humidity_2m"]

        # 3. Flatten to records (ONE record per hour per location)
        for i in range(len(times)):
            record = {
                "timestamp": datetime.fromisoformat(times[i]),
                "location_name": location["location_name"],
                "country": location["country"],
                "latitude": location["latitude"],
                "longitude": location["longitude"],
                "temperature": temperatures[i],
                "wind_speed": wind_speeds[i],
                "humidity": humidities[i]

            }
            Ingest.records.append(record)

        return Ingest.records