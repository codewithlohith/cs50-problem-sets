expression = input("Expression: ") #2 + 2

x,y,z = expression.split(" ")

x = float(x)
z = float(z)

if y == "+":
    print(round(x + z, 1))
elif y == "-":
    print(round(x - z, 1))
elif y == "*":
    print(round(x * z, 1))
elif y == "/":
    print(round(x / z, 1))
