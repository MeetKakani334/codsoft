def bi(n):
    a, b = 0, 1
    for i in range(n):
        if i == 0:
            arry.append(a)
        elif i == 1:
            arry.append(b)
        else:
            # c = a + b
            a , b = b , a + b
            arry.append(b)
n = 10
arry = []
bi(n)
print(arry)
