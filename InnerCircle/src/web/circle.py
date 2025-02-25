from fastapi import APIRouter
from model.circle import Circle
#import fake.circle as service
import service.circle as service

router = APIRouter(prefix = "/circle")

@router.get("/")
def get_all() -> list[Circle]:
    return service.get_all()

@router.get("/{radius}")
def get_one(radius) -> Circle | None:
    return service.get_one(radius)

@router.post("/")
def create(circle: Circle) -> Circle:
    return service.create(circle)

@router.patch("/")
def modify(radius: float, circle: Circle) -> Circle:
    return service.modify(radius, circle)

@router.put("/")
def replace(circle: Circle) -> Circle:
    return service.replace(circle)

@router.delete("/{radius}")
def delete(radius: float):
    return None