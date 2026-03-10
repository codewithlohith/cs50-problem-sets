import pytest
from working import convert

def test_basic():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"

def test_min():
    assert convert("8:30 AM to 5:30 PM") == "08:30 to 17:30"

def test_noon():
    assert convert("12:01 PM to 9:07 PM") == "12:01 to 21:07"

def test_night():
    assert convert("6 PM to 5:30 AM") == "18:00 to 05:30"

def test_invalid():
    with pytest.raises(ValueError):
        convert("121:01 AM to 5:30 PM")
    with pytest.raises(ValueError):
        convert("6-00 AM to 1-30 PM")
    with pytest.raises(ValueError):
        convert("9 AM  7 PM")
