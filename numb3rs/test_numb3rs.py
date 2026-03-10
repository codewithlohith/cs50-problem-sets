from numb3rs import validate


def test_valid_ipv4():
    assert validate("127.1.1.1") is True
    assert validate("255.255.255.255") is True
    assert validate("0.0.0.0") is True


def test_invalid_range():
    assert validate("256.1.1.1") is False
    assert validate("217.1.1.444") is False


def test_invalid_format():
    assert validate("1.2.3") is False
    assert validate("1.2.3.4.5") is False


def test_non_ipv4():
    assert validate("cat") is False
    assert validate("2001:0db8:85a3:0000:0000:8a2e:0370:7334") is False
