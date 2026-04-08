import requests
from config.settings import BASE_URL, AUTH, BOARD_ID

def get_lists() -> dict:
    """Retorna todas as listas do board."""
    r = requests.get(f"{BASE_URL}/boards/{BOARD_ID}/lists", params=AUTH)
    return {"lists": [{"id": l["id"], "name": l["name"]} for l in r.json()]}