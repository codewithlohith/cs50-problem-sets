name = input("camelCase: ")

for i in name:
    if i.isupper():
        print("", end = "_")
        print(i.lower(), end = "")
    else:
        print(i, end = "")
