import requests
from config.settings import BASE_URL, AUTH, BOARD_ID
from tools.lists import get_lists

def summarize_board() -> dict:
    """Retorna contagem de cards por lista."""
    lists = get_lists()["lists"]
    cards = requests.get(f"{BASE_URL}/boards/{BOARD_ID}/cards", params=AUTH).json()
    summary = {l["name"]: sum(1 for c in cards if c["idList"] == l["id"]) for l in lists}
    return {"board_summary": summary, "total_cards": len(cards)}