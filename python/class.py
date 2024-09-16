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
    Name = ''
    Math = 0.0
    Eng = 0.0
    SS = 0.0
    Sci = 0.0
    Guj = 0.0
    Snk = 0.0

    def shoe_result(self):
        print(f"Show Result:\n Math:- {self.Math},\n Eng :- {self.Eng},\n SS  :- {self.SS},\n Sci :- {self.Sci},\n Guj :- {self.Guj},\n Snk :- {self.Snk}\n")
        total_mark = self.Math + self.Eng + self.SS + self.Sci + self.Guj + self.Snk
        print("This Is Your Final Markshit\n")
        per = (total_mark/600)*100
        print(f"Your Total Mark Is:- {total_mark}")
        print(f"Your Percentage Is:- {per:.2f}%")
        if per <= 100 and per > 90:
            print("Congratulations Your Grad is (A+)")
        elif per <= 90 and per > 80:
            print("Congratulations Your Grad is (A)")
        elif per <= 80 and per > 70:
            print("Congratulations Your Grad is (B+)")
        elif per <= 70 and per > 60:
            print("Congratulations Your Grad is (B)")
        elif per <= 60 and per > 50:
            print("Congratulations Your Grad is (C+)")
        elif per <= 50 and per > 40:
            print("Congratulations Your Grad is (C)")
        elif per <= 40 and per > 33:
            print("Congratulations Your Grad is (D)")
        else:
            print("Soory You Are Fali Please Try Again Better Luck For Next Time")
            
my_result = result()
my_result.Name = print("Please Enter The Mark's According To SubJect")
my_result.Math = float(input("Enter Your Mathematics Mark Out Of 100   :- "))
my_result.Eng  = float(input("Enter Your English Mark Out Of 100       :- "))
my_result.SS   = float(input("Enter Your Social Science Mark Out Of 100:- "))
my_result.Sci  = float(input("Enter Your Science Mark  Out Of 100      :- "))
my_result.Guj  = float(input("Enter Your Gujarati (FL) Mark  Out Of 100:- "))
my_result.Snk  = float(input("Enter Your Sanskrit (SL) Mark  Out Of 100:- "))

my_result.shoe_result()




