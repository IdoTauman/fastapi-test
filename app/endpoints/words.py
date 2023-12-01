from fastapi import APIRouter
from app.services.words_client import words_client


router = APIRouter()

@router.get("/get_random")
def get_random():
    return words_client.random_word()


@router.get("/get_multiple_random")
def get_multiple_random():
    return words_client.random_words()
