from seasons import get_date_of_birth
from datetime import date
import pytest

def test_valid():
    assert get_date_of_birth("2000-01-01") == date(2000,1,1)
    assert get_date_of_birth("1999-12-31") == date(1999,12,31)

def test_invalid():
    with pytest.raises(ValueError):
        get_date_of_birth("January 1, 2000")

    with pytest.raises(ValueError):
        get_date_of_birth("2000-13-01")

    with pytest.raises(ValueError):
        get_date_of_birth("cat")
