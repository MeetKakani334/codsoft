# filter odd and even number in different list

from ast import Num


num = [1,2,3,4,5,6,7,8,9,10]
a = []
b = []

for i in num:
    if i%2 == 0:
        a.append(i)
    else:
        b.append(i)
print(a,"and",b)