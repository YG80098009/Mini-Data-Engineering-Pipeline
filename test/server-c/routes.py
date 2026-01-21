from fastapi import APIRouter
from service import save_data, get_avg_temp, get_max_wind

router = APIRouter()

@router.post("/records")
def store_records(data):
    save_data(data)
    return {"status": "saved successfully"}

@router.get('/records/avg-temperature')
def avg_temp():
    return get_avg_temp()

@router.get("/records/max-wind")
def max_wind():
    return get_max_wind()