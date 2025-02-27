from model.circle import Circle
from service import circle as code

sample = Circle(radius=47.11)

def test_create():
    resp = code.create(sample)
    assert resp == sample

def test_get_exists():
    resp = code.get_one(47.11)
    assert resp == sample

def test_get_missing():
    resp = code.get_one(47.13)
    assert resp is None