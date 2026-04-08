from google.adk.agents import Agent
from tools.cards import create_card, move_card, search_cards
from tools.lists import get_lists
from tools.board import summarize_board

root_agent = Agent(
    model="gemini-2.5-flash",
    name="trello_agent",
    instruction="""Você é um assistente de gerenciamento de projetos no Trello.
    Você pode criar cards, mover cards entre listas, buscar cards e resumir o board.
    Sempre confirme as ações realizadas e seja objetivo nas respostas.""",
    tools=[get_lists, create_card, move_card, search_cards, summarize_board],
)