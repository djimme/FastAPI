import sqlite3
from model.creature import Creature

DB_NAME = "cryptid.db"
conn = sqlite3.connect(database=DB_NAME)
curs = conn.cursor()

def init():
    curs.execute(sql="create table creature(name, description, country, area, aka)")

def row_to_model(row:tuple) -> Creature:
    name, description, country, area, aka = row
    return Creature(
        name = name, 
        description= description,
        country= country,
        area= area,
        aka= aka
    )