from fastapi import APIRouter
from app.endpoints.item import router as item_router
from app.endpoints.user import router as user_router


router = APIRouter()

router.include_router(item_router, prefix="/item", tags=["Item"])
router.include_router(user_router, prefix="/user", tags=["User"])
