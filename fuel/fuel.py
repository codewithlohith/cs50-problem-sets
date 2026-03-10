while True:
    try:
        x,y = input("Fraction: ").split("/")
        x,y = int(x), int(y)

        if (x > y or x < 0):
            continue
        else:
            result = round(x/y * 100)
            break
    except ValueError:
        pass
    except ZeroDivisionError:
        pass

if (result <= 1):
    print("E")
elif(result >= 99):
    print("F")
else:
    print(f"{result}%")

