def main():
    word = input("Input: ")
    ans = shorten(word)
    print(ans)


def shorten(word):
    ans = ""
    for letter in word:
        if letter.lower() not in ['a','e','i','o','u']:
            ans += letter

    return ans


if __name__ == "__main__":
    main()
