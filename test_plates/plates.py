def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if not s[0:2].isalpha():
        return False

    if not s.isalnum():
        return False

    if not (2 <= len(s) <= 6):
        return False

    number_started = False

    for letter in s:
        if letter.isdigit():
            if not number_started:
                if letter == '0':
                    return False
                number_started = True
        #It only comes here if it's a char and not a digit.
        else:
            if number_started == True:
                return False

    return True

if __name__ == "__main__":
    main()
