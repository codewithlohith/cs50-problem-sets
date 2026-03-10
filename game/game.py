import random

while True:
    n = int(input("Level: "))

    if (n <= 0):
        continue
    else:
        break


generate = random.randint(1,n)

while True:
    try:
        guess = int(input("Guess: "))

        if (guess <= 0):
            continue

        if (guess < generate):
            print("Too small!")
            continue

        elif (guess > generate):
            print("Too large!")
            continue

        else:
            print("Just right!")
            break

    except ValueError:
        pass

