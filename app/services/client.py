import requests


class client:
    def __init__(self, baseURL: str, apiKey: str) -> None:
        self.baseURL = baseURL
        self.apiKey = apiKey


    def RandomWord(self):
        r = requests.get(f"{self.baseURL}/getRandom", headers= {"X-RapidAPI-Key": self.apiKey, "X-RapidAPI-Host": "random-words5.p.rapidapi.com"})
        return r.text
    
    def RandomWords(self):
        r = requests.get(f"{self.baseURL}/getMultipleRandom", params={"count": "5"},headers= {"X-RapidAPI-Key": self.apiKey, "X-RapidAPI-Host": "random-words5.p.rapidapi.com"})
        return r.text
