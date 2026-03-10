from fuel import convert, gauge
import pytest

def test_convert():
    assert convert("2/4") == 50
    assert convert("3/4") == 75

def test_convert_value_error():
    with pytest.raises(ValueError):
        convert("hi")

    with pytest.raises(ValueError):
        convert("6/2")

    with pytest.raises(ValueError):
        convert("-2/4")

def test_convert_zero_division():
    with pytest.raises(ZeroDivisionError):
        convert("4/0")

def test_gauge():
    assert gauge(50) == "50%"

def test_gauge_empty():
    assert gauge(0) == "E"
    assert gauge(1) == "E"

def test_gauge_full():
    assert gauge(99) == "F"
    assert gauge(100) == "F"
