# class wedding:
#     def __init__(self,male,female,age):
#         self.male = male
#         self.female = female
#         if age >= 18:
#             self.age = age
#         else:
#             self.age = "Your Not Eligible "
#     def blessing(self):
#         print(f"You wiil Married With {self.male} And Your Age Is {self.age} You Will married with {self.female}")

# first = wedding("manmeet","sinchi",24)
# second = wedding("raj","triptidimri",21)

# first.blessing()
# second.blessing()
        
class a:
    def __init__(self,name):
        self.name = name
class b(a):
    def __init__(self,name,age):
        super().__init__(name)
        self.age = age
    def printt(self):
        print(f"{self.name}{self.age}")

c = b("meet",19)
c.printt()


