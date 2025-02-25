from model.circle import Circle
#from fake import circle as data
import data.circle as data

def get_all() -> list[Circle]:
    return data.get_all()

def get_one(radius: float) -> Circle | None:
    return data.get_one(radius)

def create(circle: Circle) -> Circle:
    return data.create(circle)

def replace(oldRadius: float, newCircle: Circle) -> Circle:
    return data.replace(oldRadius, newCircle)

def modify(radius, circle: Circle) -> Circle:
    return data.modify(radius, circle)

def delete(radius, circle: Circle) -> bool:
    return data.delete(radius)
