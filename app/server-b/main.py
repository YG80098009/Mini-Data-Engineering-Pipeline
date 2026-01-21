from fastapi import APIRouter, FastAPI

app = FastAPI()
router = APIRouter()


@router.get("/")
async def root():
    return {"hello": "world"}


app.include_router(router)

