def main():
    word = input("Input: ")
    ans = shorten(word)
    print(ans)


def shorten(word):
    ans = ""
    for letter in word:
        if letter.lower() in ['a','e','i','o','u']:
            continue
        else:
            ans += letter

    return ans


if __name__ == "__main__":
    main()
