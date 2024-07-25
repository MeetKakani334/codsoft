from ast import And, Or


a = {1,2,3,4,5,6,7,8,9,10}
a.add(11)
a.remove(3)
print (a)
b = {1,2,3,4,5,6,9,10,11,12,13,14,15,16,17,18,19,20}
a.extend(b)
print (a)

# b = {1,2,3,4}
# c = {1,2,3,4,5}
# d = b and c
# print(d)