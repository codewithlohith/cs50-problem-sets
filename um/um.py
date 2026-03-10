import re
import sys


def main():
    print(count(input("Text: ")))


def count(s):
    pattern = r'\bum\b'
    value = re.findall(pattern,s.lower())
    return len(value)


if __name__ == "__main__":
    main()
