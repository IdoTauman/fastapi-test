from fastapi import APIRouter
from app.endpoints.item import router as item_router


router = APIRouter()

router.include_router(item_router, prefix="/item", tags=["Item"])
