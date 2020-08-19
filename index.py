from fastapi import FastAPI,Response
from cla import Player
from function import cache

app = FastAPI()

@app.get("/csgo/plugin")
async def entry(steamid:str,rankid:int,svg:bool=False):
    a = Player(steamid)
    output = cache(a,rankid)
    if not svg:
        return Response(content=output,media_type='text/html')
    else:
        rep = """<svg width="750" height="360" version="1.1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
  <title>CSGO Plugin</title>
  <foreignObject width="500" height="220">
  <body xmlns="http://www.w3.org/1999/xhtml">{}</body></foreignObject>
</svg>""".format(output)
        return Response(content=rep,media_type='image/svg+xml')