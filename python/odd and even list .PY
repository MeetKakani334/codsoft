a = 1
b = []
c = []

while a <= 15:
    if a%2 == 0:
        b.append(a)
    else:
        c.append(a)
    a = a + 1
print(b,c)