from fastapi import APIRouter, Body
from service import save_data, get_avg_temp, get_max_wind

router = APIRouter()

@router.post("/records")
def store_records(data: list = Body(...)):
    save_data(data)
    return {"status": "saved successfully"}

@router.get('/records/avg-temperature')
def avg_temp():
    return get_avg_temp()

@router.get("/records/max-wind")
def max_wind():
    return get_max_wind()