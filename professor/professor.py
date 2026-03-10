import random

def main():
    level = get_level()
    score = 0
    for i in range(10):

        num1 = generate_integer(level)
        num2 = generate_integer(level)
        sum = num1 + num2
        count = 0

        for j in range(3):
            print(f"{num1} + {num2} = ", end = "")
            ans = int(input())

            if (ans == sum):
                score += 1
                count = 1
                break

            else:
                print("EEE")

        if count == 0:
            print(f"{num1} + {num2} = {sum}")

    print(f"Score: {score}")


def get_level():
    while True:
        try:
            n = int(input("Level: "))

            if n in [1,2,3]:
                return n

            else:
                continue

        except ValueError:
            pass


def generate_integer(level):
    if level not in [1,2,3]:
        raise ValueError

    if (level == 1):
        return random.randint(0,9)
    elif (level == 2):
        return random.randint(10,99)
    else:
        return random.randint(100,999)


if __name__ == "__main__":
    main()
