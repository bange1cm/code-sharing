from model.circle import Circle

_circles = [
    Circle(radius=47.11),
    Circle(radius=08.15),
    Circle(radius=5.4),
    Circle(radius=3.14),
    Circle(radius=1.618),
]

def get_all() -> list[Circle]:
    """Return all circles"""
    return _circles

def get_one(radius: float) -> Circle | None:
    for _circle in _circles:
        if (float(_circle.radius) == float(radius)):
            return _circle
    return None

# The following are nonfunctional for now,
# so they just act like they work, without modifying
# the actual fake _circles list:
def create(circle: Circle) -> Circle:
    """Add a circle"""
    return circle

def modify(circle: Circle) -> Circle:
    """Modify a circle"""
    return circle

def replace(circle: Circle) -> Circle:
    """Replace a circle"""
    return circle

def delete(radius: float) -> bool:
    """Delete a circle; return None if it existed"""
    return None