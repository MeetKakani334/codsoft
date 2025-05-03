# Desien

row = 7

for i in range(row):
    for j in range(row):
        if i == j or j == row-1-i:
            print("*", end= "")
        else:
            print(" ", end = "")
    print("")




# a = list(input("Enter The Element Of List:-"))
a = [1,2,3,4] # that is a main array 
b = [] # that is a empty array 

for i in a:
    b = [i] + b
print(b)


# that loops is Iterates through each character i in list a
#At each step, it adds i to the beginning of list b 
# ex :- i = '1' → b = ['1'] + [] → b = ['1']
#i = '2' → b = ['2'] + ['1'] → b = ['2', '1']


# same as to string 


c = "Hello"
d = ""

for i in c:
    d = i + d 
print(d)


# same as to tupel 

e = (1,2,3)
f = ()

for i in e:
    f = (i,) + f
print(f)

# error solving 

# ex:1

# data = [10, 20, 30, '40', 50]

# total = 0
# for num in data:
#     total += num

# print("Total:", total)


#  Using an Index Out of Range

# numbers = [1, 2, 3, 4, 5]

# for i in range(6):
#     print(numbers[i])

#  3) Modifying a List While Iterating Over It
# numbers = [1, 2, 3, 4, 5]

# for num in numbers:
#     if num == 3:
#         numbers.remove(num)  # List ko modify kar rahe hain while iterating

# print(numbers)


# Traditional loop
squares = []
for i in range(5):
    squares.append(i ** 2)

# List comprehension
squares = [i ** 2 for i in range(5)]




