import os
from dotenv import load_dotenv

load_dotenv()

TRELLO_API_KEY = os.getenv("TRELLO_API_KEY")
TRELLO_TOKEN   = os.getenv("TRELLO_TOKEN")
BOARD_ID       = os.getenv("TRELLO_BOARD_ID")
BASE_URL       = "https://api.trello.com/1"
AUTH           = {"key": TRELLO_API_KEY, "token": TRELLO_TOKEN}