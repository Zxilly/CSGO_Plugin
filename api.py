from fastapi import FastAPI
from typing import Optional

app = FastAPI()

@app.get("/csgo/plugin")
async def entry(steamid:str,rankid:int):
    argument = {"steamid":steamid,"rankid":rankid}
    return argument