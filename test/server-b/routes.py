from fastapi import APIRouter
import requests
from service import clean_and_transform

URL_service_c = "http://localhost:8001/records"
router = APIRouter()

@router.post("/clean")
def clean_endpoint(data):  
    final_data = clean_and_transform(data)

    response = requests.post(URL_service_c, json=final_data)

    return {"status": "sent", "response": response.status_code}