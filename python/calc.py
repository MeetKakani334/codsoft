a = int(input("enter your first number"))
b = str(input("enter your symbol"))
c = int(input("enter your second number"))

if b == "+":
    print(a + c)
elif b == "-":
    print(a - c)
elif b == "*":
    print(a * c)
elif b == "/":
    print(a / c)
else:
    print("enter your corrct symbol")