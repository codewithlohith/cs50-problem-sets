from um import count

def test_um():
    assert count("um?") == 1
    assert count("Um, thanks for the album.") == 1

def test_um_mult():
    assert count("Um, thanks, um...") == 2

def test_invalid():
    assert count("yummy") == 0
