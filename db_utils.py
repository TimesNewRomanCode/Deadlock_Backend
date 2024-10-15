import psycopg2

conn = psycopg2.connect(
        dbname="verceldb",
        user="default",
        password="93imEqtgGxpV",
        host="ep-patient-sun-a2t0s3kr-pooler.eu-central-1.aws.neon.tech",
        port="5432"
    )
cur = conn.cursor()


HeroInfo = []
ItemsInfo = []
MapInfo = []

cur.execute("SELECT * FROM Hero")
row = cur.fetchone()

def SendHeroInfo():
    Hero = {
        "id": row[0],
        "name": row[1],
        "text": row[2],
        "img": row[3],
        "DPS": row[4],
        "BulletDamage": row[5],
        "Ammo": row[6],
        "BulletPerSec": row[7],
        "ReloadTime": row[8],
        "BulletVelocity": row[9],
        "LightMelee": row[10],
        "HeavyMelee": row[11],
        "FalloffRange": row[12],
        "Health": row[13],
        "HealthRegen": row[14],
        "BulletResist": row[15],
        "SpiritResist": row[16],
        "MoveSpeed": row[17],
        "SprintSpeed": row[18],
        "Stamina": row[19]
    }
    HeroInfo.append(Hero)
    print(HeroInfo)
    return HeroInfo


def SendItemsInfo():
    Items = {
        "id": row[0],
        "name": row[1],
        "prise": row[2],
        "text": row[3],
        "img": row[4],
        "effect": row[5],
        "effectTextP": row[6],
        "effectTextA": row[7]
    }
    ItemsInfo.append(Items)
    return ItemsInfo

def SendMapInfo():
    Map = {
        "id": row[0],
        "name": row[1],
        "text": row[2],
        "img": row[3]
    }

    MapInfo.append(Map)
    return MapInfo

