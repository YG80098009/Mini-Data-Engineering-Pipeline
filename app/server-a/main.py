from service.ingest_weather import Ingest 

data = Ingest.ingest_weather_for_location("London")
print(data)