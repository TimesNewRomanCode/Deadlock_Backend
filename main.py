from fastapi import FastAPI
from db_utils import SendHeroInfo, SendItemsInfo, SendMapInfo
import psycopg2
from models import HeroInfo, ItemInfo, MapInfo

conn = psycopg2.connect(
        dbname="verceldb",
        user="default",
        password="93imEqtgGxpV",
        host="ep-patient-sun-a2t0s3kr-pooler.eu-central-1.aws.neon.tech",
        port="5432"
    )

cur = conn.cursor()

app = FastAPI()

# этот код отправляет все данные с таблицы
@app.get("/Hero")
def HeroInfoGet():
    return {"data": SendHeroInfo()}

@app.get("/Items")
def ItemsInfoGet():
    return {"data": SendItemsInfo()}

@app.get("/Map")
def MapInfoGet():
    return {"data": SendMapInfo()}

# Следующий код создаёт строку в таблице
@app.post("/Heroes")
async def create_hero(hero: HeroInfo):
    insert_query = """INSERT INTO Hero (id, name, text, img, DPS, BulletDamage, Ammo, BulletPerSec, ReloadTime, BulletVelocity, LightMelee, HeavyMelee, FalloffRange, Health, HealthRegen, BulletResist, SpiritResist, MoveSpeed, SprintSpeed, Stamina)
                      VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);"""
    cur.execute(insert_query,
                (hero.id, hero.name, hero.text, hero.img, hero.DPS, hero.BulletDamage, hero.Ammo, hero.BulletPerSec, hero.ReloadTime, hero.BulletVelocity, hero.LightMelee, hero.HeavyMelee, hero.FalloffRange, hero.Health, hero.HealthRegen, hero.BulletResist, hero.SpiritResist, hero.MoveSpeed, hero.SprintSpeed, hero.Stamina))
    conn.commit()
    return hero

@app.post("/Items")
async def create_item(item: ItemInfo):
    insert_query = """INSERT INTO Items (id, name, price, text, img, effect, effectTextP, effectTextA)
                      VALUES (%s, %s, %s, %s, %s, %s, %s, %s);"""

    cur.execute(insert_query,
                (item.id, item.name, item.price, item.text, item.img, item.effect, item.effectTextP, item.effectTextA))
    conn.commit()
    return item

@app.post("/Maps")
async def create_map(map_info: MapInfo):
    insert_query = """INSERT INTO Map (id, name, text, img)
                      VALUES (%s, %s, %s, %s);"""

    cur.execute(insert_query, (map_info.id, map_info.name, map_info.text, map_info.img))
    conn.commit()
    return map_info

# Следующий код обновляет информацию в таблице
@app.post("/HeroesUP/{id}")
async def update_hero(id: int, hero: HeroInfo):
    update_query = """UPDATE Hero 
                      SET name = %s, text = %s, img = %s, DPS = %s, BulletDamage = %s, Ammo = %s, BulletPerSec = %s, ReloadTime = %s, BulletVelocity = %s, LightMelee = %s, HeavyMelee = %s, FalloffRange = %s, Health = %s, HealthRegen = %s, BulletResist = %s, SpiritResist = %s, MoveSpeed = %s, SprintSpeed = %s, Stamina = %s 
                      WHERE id = %s;"""
    cur.execute(update_query,
                (hero.name, hero.text, hero.img, hero.DPS, hero.BulletDamage, hero.Ammo, hero.BulletPerSec, hero.ReloadTime, hero.BulletVelocity, hero.LightMelee, hero.HeavyMelee, hero.FalloffRange, hero.Health, hero.HealthRegen, hero.BulletResist, hero.SpiritResist, hero.MoveSpeed, hero.SprintSpeed, hero.Stamina, id))
    conn.commit()
    return hero

@app.post("/HeroesUP/{id}")
async def update_hero(id: int, hero: HeroInfo):
    update_query = """UPDATE Hero 
                      SET name = %s, text = %s, img = %s, DPS = %s, BulletDamage = %s, Ammo = %s, BulletPerSec = %s, ReloadTime = %s, BulletVelocity = %s, LightMelee = %s, HeavyMelee = %s, FalloffRange = %s, Health = %s, HealthRegen = %s, BulletResist = %s, SpiritResist = %s, MoveSpeed = %s, SprintSpeed = %s, Stamina = %s 
                      WHERE id = %s;"""
    cur.execute(update_query,
                (hero.name, hero.text, hero.img, hero.DPS, hero.BulletDamage, hero.Ammo, hero.BulletPerSec, hero.ReloadTime, hero.BulletVelocity, hero.LightMelee, hero.HeavyMelee, hero.FalloffRange, hero.Health, hero.HealthRegen, hero.BulletResist, hero.SpiritResist, hero.MoveSpeed, hero.SprintSpeed, hero.Stamina, id))
    conn.commit()
    return hero


@app.post("/HeroesUP/{id}")
async def update_hero(id: int, hero: HeroInfo):
    update_query = """UPDATE Hero 
                      SET name = %s, text = %s, img = %s, DPS = %s, BulletDamage = %s, Ammo = %s, BulletPerSec = %s, ReloadTime = %s, BulletVelocity = %s, LightMelee = %s, HeavyMelee = %s, FalloffRange = %s, Health = %s, HealthRegen = %s, BulletResist = %s, SpiritResist = %s, MoveSpeed = %s, SprintSpeed = %s, Stamina = %s 
                      WHERE id = %s;"""
    cur.execute(update_query,
                (hero.name, hero.text, hero.img, hero.DPS, hero.BulletDamage, hero.Ammo, hero.BulletPerSec, hero.ReloadTime, hero.BulletVelocity, hero.LightMelee, hero.HeavyMelee, hero.FalloffRange, hero.Health, hero.HealthRegen, hero.BulletResist, hero.SpiritResist, hero.MoveSpeed, hero.SprintSpeed, hero.Stamina, id))
    conn.commit()
    return hero
# uvicorn main:app --reload
# git commit -m "Commit message"
# git push -u origin main