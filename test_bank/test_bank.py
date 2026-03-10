from bank import value

def test_hello():
    assert value("hello, world") == 0

def test_h():
    assert value("hey") == 20

def test_not_h():
    assert value("David") == 100

def test_capital():
    assert value("HELLO, WORLD") == 0

