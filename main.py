from fastapi import FastAPI
from db_utils import SendHeroInfo, SendItemsInfo, SendMapInfo

app = FastAPI()

@app.get("/Hero")
def HeroInfoGet():
    return {"data": SendHeroInfo()}

@app.get("/Items")
def ItemsInfoGet():
    return {"data": SendItemsInfo()}

@app.get("/Map")
def MapInfoGet():
    return {"data": SendMapInfo()}

