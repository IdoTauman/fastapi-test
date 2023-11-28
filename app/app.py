from fastapi import FastAPI, APIRouter
from app.schemas.item import Item
from app.endpoints.api_routers import router

app = FastAPI()

app.include_router(router)
