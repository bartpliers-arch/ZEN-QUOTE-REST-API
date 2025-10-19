from dataclasses import dataclass
import requests

counter = 0

@dataclass
class Quote:
    id_q: int
    q: str
    a: str

def quotes_api():
    global counter
    counter  += 1
    response = requests.get("https://zenquotes.io/api/random")
    data = response.json()[0]
    structure = {
        "id_q": counter,
        "q": data["q"],
        "a": data["a"],
    }
    return structure
