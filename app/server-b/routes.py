
from fastapi import APIRouter

from service import clean_and_transform

router = APIRouter()

@router.post('/clean')
def clean_endpoint(data):
    Final_data = clean_and_transform(data)
    return Final_data
    # requests.post(json=Final_data)

    # return jsonify({"status": "ok"})

