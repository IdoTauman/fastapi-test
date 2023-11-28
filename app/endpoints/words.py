from fastapi import APIRouter
from app.services.client import client

router = APIRouter()

@router.get("/getRandom")
def getRandom():
    APIclient = client(baseURL="https://random-words5.p.rapidapi.com", apiKey="9ef31d92a4msh85731ca38c62a57p1e7318jsn7ecaa55b0256")
    return APIclient.RandomWord()

@router.get("/getMultipleRandom")
def getMultipleRandom():
    APIclient = client(baseURL="https://random-words5.p.rapidapi.com", apiKey="9ef31d92a4msh85731ca38c62a57p1e7318jsn7ecaa55b0256")
    return APIclient.RandomWords()
