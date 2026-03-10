from plates import is_valid

def test_alpha():
    assert is_valid("hello") == True
    assert is_valid("7hello") == False

def test_alphanum():
    assert is_valid("hi67") == True
    assert is_valid("hi_67") == False

def test_length():
    assert is_valid("david123") == False

def test_number_not_at_the_end():
    assert is_valid("qw27q") == False

def test_num_beginning():
    assert is_valid("7heart") == False

def test_zero():
    assert is_valid("hell06") == False

def test_num():
    assert is_valid("12345") == False
