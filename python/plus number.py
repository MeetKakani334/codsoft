a = int(input("ENTER YOUR PLUS NUMBER :-"))
b = 0

while a > 0:
    c = a%10
    b = b + c
    a//=10
    print(b)

