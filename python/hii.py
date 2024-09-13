#1). Normal Function:
# def name():
#     print("hello")


# name()

# 2) . With Argument:

# def name(x):
#     return 5*x


# print(name(10))




# # 3).Default Argument
# def name(x=10,y=20):
#     return x + y

# print(name())


def randomargument(*data):
 print("No is :",data[0])
 print("Name is :",data[1])
 print("Address is :",data[2])
 print("Mobile is :",data[3])
randomargument(1,"Hitesh","9016395600","Ahemdabad")
