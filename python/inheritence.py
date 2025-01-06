# Singl inheritence

class Animal:
    def sound(self):
        print("This Animal Is Sound")
class dog(Animal):
    def brak(self):
        print("The Dog Braks")

Dog = dog()
Dog.sound()
Dog.brak()


# Multiple inheritence

class icecreem:
    def flavour(self):
        print("Flavour types are")
class vanilla:
    def filled(self):
        print("This Flavour is vanilla")
class cup(icecreem,vanilla):
    def large(self):
        print("your cup is ready")

call=cup()
call.flavour()
call.filled()
call.large()
    

# multilevel

class mobile:
    def compny(self):
        print("this is your compony")
class redmi(mobile):
    def compny1(self):
        print("redmi is beter than iphone")
class redmi_not_10t_5G(redmi):
    def function(self):
        print("This is 5g phoone")

phone = redmi_not_10t_5G()
phone.compny()
phone.compny1()
phone.function()


# hierarchical


class computer:
    def on(self):
        print("Your window is starting")
class moni(computer):
    def str(self):
        print("opening")
class cpu(computer):
    def end(self):
        print("your Work is done")

pc = cpu()
en = moni()

en.on()
en.str()
pc.end()






