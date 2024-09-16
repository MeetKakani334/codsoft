# class your_name:
#     first_name =""
#     last_name = ""

#     def show_name(self):
#         print(f"your name:{self.first_name} {self.last_name}")
# name = your_name()

# name.first_name = "Meet"
# name.last_name = "Kakani"

# name.show_name()





class result:
    Math = 0.0
    Eng = 0.0
    SS = 0.0
    Sci = 0.0
    Guj = 0.0
    Snk = 0.0
    def shoe_result(self):
        print(f"Show Result:Math:- {self.Math}, Eng:- {self.Eng}, SS:- {self.SS}, Sci:- {self.Sci}, Guj:- {self.Guj}, Snk:- {self.Snk}")
        total_mark = self.Math + self.Eng + self.SS + self.Sci + self.Guj + self.Snk
        per = (total_mark/700)*100
        print(f"Total Mark Is {total_mark}")
        print(f"Percentage: {per:.2f}%")
my_result = result()

my_result.Math = float(input("Enter Your Mathematics Mark Out Of 100:-"))
my_result.Eng  = float(input("Enter Your English Mark Out Of 100:-"))
my_result.SS   = float(input("Enter Your Social Science Mark Out Of 100:-"))
my_result.Sci  = float(input("Enter Your Science Mark  Out Of 100:-"))
my_result.Guj  = float(input("Enter Your Gujarati (FL) Mark  Out Of 100:-"))
my_result.Snk  = float(input("Enter Your Sanskrit (SL) Mark  Out Of 100:-"))


my_result.shoe_result()



