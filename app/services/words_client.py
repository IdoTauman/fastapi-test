import requests
from app.settings import settings


class WordsClient:
    def __init__(self, base_url: str, api_key: str) -> None:
        self.base_url = base_url
        self.api_key = api_key

    def random_word(self):
        r = requests.get(
            f"{self.base_url}/getRandom",
            headers={
                "X-RapidAPI-Key": self.api_key,
                "X-RapidAPI-Host": "random-words5.p.rapidapi.com",
            },
        )
        return r.text

    def random_words(self):
        r = requests.get(
            f"{self.base_url}/getMultipleRandom",
            params={"count": "5"},
            headers={
                "X-RapidAPI-Key": self.api_key,
                "X-RapidAPI-Host": "random-words5.p.rapidapi.com",
            },
        )
        return r.text


words_client = WordsClient(
    base_url=settings.WORDS_BASE_URL, api_key=settings.WORDS_API_KEY
)
