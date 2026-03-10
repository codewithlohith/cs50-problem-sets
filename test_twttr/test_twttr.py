from twttr import shorten

def test_lowercase_vowels():
    assert shorten("aeiou") == ""

def test_uppercase_vowels():
    assert shorten("AEIOU") == ""

def test_mixed_case():
    assert shorten("Twitter") == "Twttr"

def test_numbers_preserved():
    assert shorten("CS50") == "CS50"

def test_punctuation_preserved():
    assert shorten("Hello, world!") == "Hll, wrld!"


