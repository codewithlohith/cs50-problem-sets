inp = input("Greeting").lower().strip()

if inp.startswith("hello"):
    print("$0")
elif inp.startswith("h"):
    print("$20")
else:
    print("$100")


