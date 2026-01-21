
from fastapi import APIRouter

from service import clean_and_transform

router = APIRouter()

@router.post('/clean')
def clean_endpoint():
    Final_data = clean_and_transform()

    requests.post(json=Final_data)

    return jsonify({"status": "ok"})



router = APIRouter()


@router.get("/")
async def root():
    return {"hello": "world"}


app.include_router(router)