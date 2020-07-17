from fastapi import FastAPI,Response
from typing import Optional
from cla import Player
from pri import user_code
from function import cache

app = FastAPI()

@app.get("/csgo/plugin")
async def entry(steamid:str,rankid:int):
    a = Player(steamid)
    output = cache(a,rankid)
    return Response(content=output,media_type='text/html')