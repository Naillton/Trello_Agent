import asyncio
import os
from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService
from google.genai import types
from agent.agent import root_agent
from dotenv import load_dotenv

load_dotenv()

MAX_HISTORY_TURNS = int(os.getenv("HISTORY_TURNS", 10))


def trim_history(session, max_turns: int):
    """Mantém apenas os últimos N turnos na sessão."""
    if len(session.events) > max_turns * 2:
        session.events = session.events[:1] + session.events[-(max_turns * 2):]


async def run():
    session_service = InMemorySessionService()
    runner = Runner(agent=root_agent, session_service=session_service, app_name="trello_agent")
    session = await session_service.create_session(app_name="trello_agent", user_id="user1")

    print("Agente Trello pronto! Digite 'sair' para encerrar.\n")
    while True:
        user_input = input("Você: ").strip()
        if user_input.lower() == "sair":
            break

        trim_history(session, MAX_HISTORY_TURNS)

        content = types.Content(role="user", parts=[types.Part(text=user_input)])
        async for event in runner.run_async(user_id="user1", session_id=session.id, new_message=content):
            if event.is_final_response():
                print(f"Agente: {event.content.parts[0].text}\n")


if __name__ == "__main__":
    asyncio.run(run())