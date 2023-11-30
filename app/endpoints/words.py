from fastapi import APIRouter
from app.services.client import words_client

router = APIRouter()

@router.get("/get_random")
def getRandom():
    return words_client.Random_word()

@router.get("/get_multiple_random")
def getMultipleRandom():
    return words_client.Random_words()
