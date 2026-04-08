# Trello ADK Agent

Agente de IA para gerenciamento do Trello usando **Google ADK** e **Gemini**, desenvolvido em Python com princípios de Clean Code.

O agente entende linguagem natural e executa ações diretamente no seu board do Trello — criar cards, mover entre listas, buscar tarefas e resumir o status do board.

---

## Funcionalidades

- Criar cards em qualquer lista pelo nome
- Mover cards entre listas
- Buscar cards por palavras-chave
- Resumir o board com contagem de cards por lista
- Interface web interativa via `adk web`
- Controle de janela de contexto com `trim_history`

---

## Tecnologias

- [Google ADK](https://google.github.io/adk-docs/) — framework de agentes de IA
- [Gemini 2.5 Flash Lite](https://ai.google.dev) — modelo de linguagem
- [Trello REST API](https://developer.atlassian.com/cloud/trello/rest/) — integração com o Trello
- Python 3.11+

---

## Estrutura do projeto

```
trello-adk-agent/
├── .env                  # variáveis de ambiente (não versionar)
├── .env.example          # template das variáveis
├── requirements.txt
├── main.py               # entrypoint
├── agent/
│   ├── __init__.py       # expõe root_agent para o adk web
│   ├── agent.py          # definição do agente ADK
│   └── runner.py         # loop de conversa com trim_history
├── tools/
│   ├── __init__.py
│   ├── cards.py          # create_card, move_card, search_cards
│   ├── lists.py          # get_lists
│   └── board.py          # summarize_board
└── config/
    ├── __init__.py
    └── settings.py       # carrega variáveis de ambiente
```

---

## Pré-requisitos

- Python 3.11+
- Conta no [Google AI Studio](https://aistudio.google.com) com API Key
- Conta no Trello com API Key e Token

---

## Instalação

```bash
# clone o repositório
git clone https://github.com/seu-usuario/trello-adk-agent.git
cd trello-adk-agent

# crie e ative o ambiente virtual
python -m venv .venv
source .venv/bin/activate  # Linux/macOS
.venv\Scripts\activate     # Windows

# instale as dependências
pip install -r requirements.txt
```

---

## Configuração

Copie o arquivo de exemplo e preencha com suas credenciais:

```bash
cp .env.example .env
```

```env
# Google ADK
GOOGLE_API_KEY=sua_chave_google_aqui

# Trello
TRELLO_API_KEY=sua_chave_trello_aqui
TRELLO_TOKEN=seu_token_trello_aqui
TRELLO_BOARD_ID=id_do_seu_board_aqui

# Configurações do agente
HISTORY_TURNS=10
```

### Como obter as credenciais

**Google API Key**
1. Acesse [aistudio.google.com/apikey](https://aistudio.google.com/apikey)
2. Crie uma nova chave de API

**Trello API Key e Token**
1. Acesse [trello.com/power-ups/admin](https://trello.com/power-ups/admin)
2. Crie um novo Power-Up para obter a API Key
3. Clique em "Token" na mesma página para gerar o Token

**Trello Board ID**
1. Abra seu board no Trello
2. O ID está na URL: `trello.com/b/XXXXXXXX/nome-do-board`
3. O `XXXXXXXX` é o Board ID

---

## Como usar

### Modo terminal

```bash
python main.py
```

### Modo interface web (ADK)

```bash
adk web .
```

Acesse `http://localhost:8000` para usar a interface visual com debug de eventos e ferramentas em tempo real.

---

## Exemplos de uso

```
Você: tenho alguma tarefa pendente?
Você: cria um card chamado "Revisar PR" na lista To Do
Você: move o card "Revisar PR" para In Progress
Você: busca cards sobre deploy
Você: me dá um resumo do board
```

---

## Limites da API Gemini (free tier)

| Modelo | RPM | Req/dia |
|---|---|---|
| gemini-2.5-flash-lite | 15 | 1.000 |
| gemini-2.5-flash | 10 | 250 |
| gemini-2.5-pro | 5 | 25 |

> Os limites resetam à meia-noite no horário do Pacífico (4h no Brasil).
> Para uso intensivo, considere ativar o billing no Google AI Studio.

---

## Variáveis de ambiente

| Variável | Descrição | Obrigatório |
|---|---|---|
| `GOOGLE_API_KEY` | Chave da API do Google AI Studio | Sim |
| `TRELLO_API_KEY` | Chave da API do Trello | Sim |
| `TRELLO_TOKEN` | Token de acesso do Trello | Sim |
| `TRELLO_BOARD_ID` | ID do board do Trello | Sim |
| `HISTORY_TURNS` | Número de turnos mantidos na janela de contexto | Não (padrão: 10) |

---

## Licença

MIT