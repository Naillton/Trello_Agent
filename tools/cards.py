import requests
from config.settings import BASE_URL, AUTH, BOARD_ID
from tools.lists import get_lists

def create_card(list_name: str, card_name: str, description: str = "") -> dict:
    """Cria um card em uma lista pelo nome."""
    lists = get_lists()["lists"]
    target = next((l for l in lists if list_name.lower() in l["name"].lower()), None)
    if not target:
        return {"error": f"Lista '{list_name}' não encontrada."}
    payload = {**AUTH, "idList": target["id"], "name": card_name, "desc": description}
    r = requests.post(f"{BASE_URL}/cards", params=payload)
    card = r.json()
    return {"card_id": card["id"], "name": card["name"], "url": card["shortUrl"]}

def move_card(card_name: str, destination_list: str) -> dict:
    """Move um card para outra lista pelo nome."""
    cards = requests.get(f"{BASE_URL}/boards/{BOARD_ID}/cards", params=AUTH).json()
    card = next((c for c in cards if card_name.lower() in c["name"].lower()), None)
    if not card:
        return {"error": f"Card '{card_name}' não encontrado."}
    lists = get_lists()["lists"]
    dest = next((l for l in lists if destination_list.lower() in l["name"].lower()), None)
    if not dest:
        return {"error": f"Lista '{destination_list}' não encontrada."}
    requests.put(f"{BASE_URL}/cards/{card['id']}", params={**AUTH, "idList": dest["id"]})
    return {"moved": card["name"], "to": dest["name"]}

def search_cards(query: str) -> dict:
    """Busca cards no board pelo nome."""
    cards = requests.get(f"{BASE_URL}/boards/{BOARD_ID}/cards", params=AUTH).json()
    found = [{"name": c["name"], "url": c["shortUrl"]}
             for c in cards if query.lower() in c["name"].lower()]
    return {"results": found, "total": len(found)}