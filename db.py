import psycopg2

conn = psycopg2.connect(
        dbname="verceldb",
        user="default",
        password="93imEqtgGxpV",
        host="ep-patient-sun-a2t0s3kr-pooler.eu-central-1.aws.neon.tech",
        port="5432"
    )

cur = conn.cursor()

create_table_query_1 = """CREATE TABLE Hero (
                         id SERIAL PRIMARY KEY,
                         name VARCHAR(50),
                         text VARCHAR(200),
                         img VARCHAR(50),
                         DPS VARCHAR(50),
                         BulletDamage VARCHAR(50),
                         Ammo VARCHAR(50),
                         BulletPerSec VARCHAR(50),
                         ReloadTime VARCHAR(50),
                         BulletVelocity VARCHAR(50),
                         LightMelee VARCHAR(50),
                         HeavyMelee VARCHAR(50),
                         FalloffRange VARCHAR(50),
                         Health VARCHAR(50),
                         HealthRegen VARCHAR(50),
                         BulletResist VARCHAR(50),
                         SpiritResist VARCHAR(20),
                         MoveSpeed VARCHAR(20),
                         SprintSpeed VARCHAR(20),
                         Stamina VARCHAR(20)
                        );"""
cur.execute(create_table_query_1)

create_table_query_2 = """CREATE TABLE Items (
                         id SERIAL PRIMARY KEY,
                         name VARCHAR(50),
                         price VARCHAR(20),
                         text VARCHAR(50),
                         img VARCHAR(50),
                         effect VARCHAR(20),                       
                         effectTextP VARCHAR(20),
                         effectTextA VARCHAR(20)
                     );"""
cur.execute(create_table_query_2)

create_table_query_3 = """CREATE TABLE Map (
                         id SERIAL PRIMARY KEY,
                         name VARCHAR(50),
                         text VARCHAR(50),
                         img VARCHAR(50)                                
                     );"""
cur.execute(create_table_query_3)

conn.commit()

cur.close()
conn.close()