from fastapi import FastAPI, Request
import sqlite3
import requests
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import re

app = FastAPI()
storeCards = "card.db"




origins = ["http://127.0.0.1:5500"]  # your frontend URL

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # allow these origins
    allow_credentials=True,
    allow_methods=["*"],  # allow GET, POST, etc.
    allow_headers=["*"],  # allow headers
)


@app.get("/")
async def root():
    return {"message": "weclome to the backend"}


@app.post("/send")
async def send(request: Request):
    data = await request.json()
    print("Got from JS:", data)
    cardToDb(data)

    return {"status": "ok",}


def cardToDb(holdingData):

    conn = sqlite3.connect(storeCards)
    cur = conn.cursor()

    title = holdingData.get("title", "untitled").strip()
    if not title:
        title = "untitled"
    title = re.sub(r"\W+", "_", title)

    # Create table
    cur.execute(f'''
        CREATE TABLE IF NOT EXISTS "{title}" (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            term TEXT,
            def TEXT
        )
    ''')

    # Insert cards
    for key, card in holdingData.items():
        if key.startswith("cardDiv"):
            term = card["term"]
            definition = card["def"]
            print(term, definition)
            cur.execute(
                f'INSERT INTO "{title}" (term, def) VALUES (?, ?)',
                (term, definition)
            )

    conn.commit()
    conn.close()


@app.get("/giveCards")
async def give():
    smart()


def smart():
    conn = sqlite3.connect(storeCards)
    cur = conn.cursor()

    cur.execute("SELECT term,def")

    