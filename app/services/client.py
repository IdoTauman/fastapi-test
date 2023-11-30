import requests
from dotenv import load_dotenv
from os import getenv


load_dotenv()

class WordsClient:
    def __init__(self, base_url: str, api_key: str) -> None:
        self.base_url = base_url
        self.api_key = api_key


    def Random_word(self):
        r = requests.get(f"{self.base_url}/getRandom", headers= {"X-RapidAPI-Key": self.api_key, "X-RapidAPI-Host": "random-words5.p.rapidapi.com"})
        return r.text
    
    def Random_words(self):
        r = requests.get(f"{self.base_url}/getMultipleRandom", params={"count": "5"},headers= {"X-RapidAPI-Key": self.api_key, "X-RapidAPI-Host": "random-words5.p.rapidapi.com"})
        return r.text

words_client = WordsClient(base_url=getenv("words_base_url"), api_key=getenv("APIKEY"))
