a = int(input("enter your number:"))
re = 1
while a > 0:
    c = a % 10
    re = re * 1 * c
    a//=10
print(re)
    