from fastapi import APIRouter
from app.services.client import APIclient

router = APIRouter()

@router.get("/get_random")
def getRandom():
    return APIclient.RandomWord()

@router.get("/get_multiple_random")
def getMultipleRandom():
    return APIclient.RandomWords()
