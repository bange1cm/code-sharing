from data.init import curs
from data.init import conn
from model.circle import Circle

curs.execute("""CREATE TABLE IF NOT EXISTS circle(
                radius REAL NOT NULL PRIMARY KEY)""")


def row_to_model(row: tuple) -> Circle:
    if (row==None): # if no entry is returned
        return None
    else:
        radius = row[0]
        return Circle(radius=radius)
    
def model_to_dict(circle: Circle) -> dict:
    print(circle.model_dump())
    return circle.model_dump()

def get_one(radius: float) -> Circle:
    qry = "SELECT * FROM circle WHERE radius=:radius"
    params = {"radius": radius}
    curs.execute(qry, params)
    row = curs.fetchone()
    return row_to_model(row)

def get_all() -> list[Circle]:
    qry = "SELECT * FROM circle"
    curs.execute(qry)
    rows = list(curs.fetchall())
    return [row_to_model(row) for row in rows]

def create(circle: Circle):
    qry = """INSERT OR IGNORE INTO circle VALUES (:radius)""" # Ignore if duplicate, we can do for single value entry
    params = model_to_dict(circle)
    curs.execute(qry, params)
    conn.commit()
    return circle

def modify(radius: float, circle: Circle) -> Circle:
    qry = """update circle set
             radius=:radius
             where radius=:orig_radius"""
    params = model_to_dict(circle)
    params["orig_radius"] = radius
    curs.execute(qry, params)
    return get_one(circle)

def replace(oldRadius: float, newCircle: Circle) -> Circle:
    qry = """update circle
    set radius=:radius
    where radius=:radius_orig"""
    params = model_to_dict(newCircle)
    params["radius_orig"] = oldRadius
    _ = curs.execute(qry, params)
    return get_one(newCircle)

def delete(circle: Circle):
    qry = "DELETE FROM circle WHERE radius=:radius"
    params = {"radius": circle.radius}
    curs.execute(qry, params)
    conn.commit()