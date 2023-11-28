import requests
from dotenv import load_dotenv
from os import getenv


load_dotenv()

class WordsClient:
    def __init__(self, base_url: str, apiKey: str) -> None:
        self.base_url = base_url
        self.apiKey = apiKey


    def RandomWord(self):
        r = requests.get(f"{self.base_url}/getRandom", headers= {"X-RapidAPI-Key": self.apiKey, "X-RapidAPI-Host": "random-words5.p.rapidapi.com"})
        return r.text
    
    def RandomWords(self):
        r = requests.get(f"{self.base_url}/getMultipleRandom", params={"count": "5"},headers= {"X-RapidAPI-Key": self.apiKey, "X-RapidAPI-Host": "random-words5.p.rapidapi.com"})
        return r.text

APIclient = WordsClient(base_url="https://random-words5.p.rapidapi.com", apiKey=getenv("APIKEY"))
