from .init import curs
from model.explorer import Explorer

curs.execute("""create table if not exists explorer(
                name text primary key,
                country text,
                description text)""")

def row_to_model(row: tuple) -> Explorer:
    name, country, description = row
    return Explorer(
        name = name, 
        country=country, 
        description=description)

def model_to_dict(explorer: Explorer) -> dict:
    return explorer.model_dump() if explorer else None

def get_one(name: str) -> Explorer:
    qry = "select * from explorer where name=:name"
    params = {"name":name}
    curs.execute(qry, params)
    row = curs.fetchone()
    return row_to_model(row)

def get_all() -> list[Explorer]:
    qry = "select * from explorer"
    rows = curs.fetchall()
    return [row_to_model(row) for row in rows]

def create(explorer: Explorer) -> Explorer:
    qry = """insert into explorer (name, country, description)
            values (:name, :country, :description)"""
    params = model_to_dict(explorer)
    _ = curs.execute(qry, params)
    return get_one(explorer.name)

def modify(explorer: Explorer) -> Explorer:
    qry = """update explorer 
            set country=:country,
                name=:name,
                description=:description
                where name=:name_orig"""
    
    params = model_to_dict(explorer)
    params["name_orig"] = explorer.name
    _ = curs.execute(qry, params)
    return get_one(explorer.name)

def delete(explorer:Explorer) -> bool:
    qry = "delete from explorer where name=:name"
    params = {"name":explorer.name}
    res = curs.execute(qry, params)
    return bool(res)