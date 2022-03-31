def add(a, b):
    return a + b

def subtract(a,b):
    return a-b


def test_add():
    assert add(2, 3) == 5
    assert add('space', 'ship') == 'spaceship'
    assert add(0.1,0.2) - 0.3 < 1e-6

def test_subtract():
    assert subtract(1-1) == 0