from fastapi import APIRouter
from app.schemas.item import Item


router = APIRouter()


@router.get("/{item_id}")
def get_item(item_id: str):
    return {"item": item_id}


@router.get("")
def list_items():
    return []


@router.post("")
def create_item(item: Item):
    return item


@router.put("")
def update_item(item: Item):
    return item


@router.delete("/{item_id}")
def delete_item(item_id: str):
    return item_id
