from fastapi import FastAPI
from typing import Optional
from cla import Player
from pri import user_code
from function import render

app = FastAPI()

@app.get("/csgo/plugin")
async def entry(steamid:str,rankid:int):
    a = Player(user_code)
    output = render(a,6)
    return output