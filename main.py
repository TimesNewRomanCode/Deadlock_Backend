from fastapi import FastAPI, Request
from db_utils import SendHeroInfo, SendItemsInfo, SendMapInfo
from typing import List
import json
import psycopg2
from pydantic import BaseModel

conn = psycopg2.connect(
        dbname="verceldb",
        user="default",
        password="93imEqtgGxpV",
        host="ep-patient-sun-a2t0s3kr-pooler.eu-central-1.aws.neon.tech",
        port="5432"
    )

cur = conn.cursor()

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

class HeroInfo(BaseModel):
    id: int
    name: str
    text: str
    img: str
    DPS: str
    BulletDamage: str
    Ammo: str
    BulletPerSec: str
    ReloadTime: str
    BulletVelocity: str
    LightMelee: str
    HeavyMelee: str
    FalloffRange: str
    Health: str
    HealthRegen: str
    BulletResist: str
    SpiritResist: str
    MoveSpeed: str
    SprintSpeed: str
    Stamina: str

@app.post("/Heroes")
async def create_hero(hero: HeroInfo):
    insert_query = """INSERT INTO Hero (id, name, text, img, DPS, BulletDamage, Ammo, BulletPerSec, ReloadTime, BulletVelocity, LightMelee, HeavyMelee, FalloffRange, Health, HealthRegen, BulletResist, SpiritResist, MoveSpeed, SprintSpeed, Stamina)
                      VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);"""
    cur.execute(insert_query,
                (hero.id, hero.name, hero.text, hero.img, hero.DPS, hero.BulletDamage, hero.Ammo, hero.BulletPerSec, hero.ReloadTime, hero.BulletVelocity, hero.LightMelee, hero.HeavyMelee, hero.FalloffRange, hero.Health, hero.HealthRegen, hero.BulletResist, hero.SpiritResist, hero.MoveSpeed, hero.SprintSpeed, hero.Stamina))
    conn.commit()

class ItemInfo(BaseModel):
    id: int
    name: str
    price: str
    text: str
    img: str
    effect: str
    effectTextP: str
    effectTextA: str

@app.post("/Items")
async def create_item(item: ItemInfo):
    insert_query = """INSERT INTO Items (id, name, price, text, img, effect, effectTextP, effectTextA)
                      VALUES (%s, %s, %s, %s, %s, %s, %s, %s);"""

    cur.execute(insert_query,
                (item.id, item.name, item.price, item.text, item.img, item.effect, item.effectTextP, item.effectTextA))
    conn.commit()

    print(item)
    return item


# uvicorn main:app --reload





git init
git remote add origin https://github.com/TimesNewRomanCode/Deadlock_Backend.git
git checkout main
git push -u origin maingi