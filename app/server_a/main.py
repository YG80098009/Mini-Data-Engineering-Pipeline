from fastapi import FastAPI 
from schema import Ingest
from service import ingest_weather_for_location
app = FastAPI()

@app.post("/ingest")
def ingest(ingest: Ingest):
    data = ingest_weather_for_location(ingest.location_name)
    return data 
