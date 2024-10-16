from pydantic import BaseModel

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

class ItemInfo(BaseModel):
    id: int
    name: str
    price: str
    text: str
    img: str
    effect: str
    effectTextP: str
    effectTextA: str

class MapInfo(BaseModel):
    id: int
    name: str
    text: str
    img: str