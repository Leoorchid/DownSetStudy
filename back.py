from fastapi import FastAPI, Request
import sqlite3
import requests
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import re

app = FastAPI()
storeCards = "card.db"

conn = sqlite3.connect(storeCards)
cur = conn.cursor()


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
    title = f"{re.sub(r"\W+", "_", data["title"])}"

    cur.execute(
        f"""

    CREATE TABLE IF NOT EXISTS {title}(

                id INTEGER PRIMARY KEY AUTOINCREMENT,
                term TEXT,
                def TEXT   
                
                )
        """
    )
    conn.commit()

    for u in data:
        print(data[u])

    conn.commit()

    return {"status": "ok", "d": data}
