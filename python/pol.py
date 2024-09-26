# class tarang_sir:
#     def main(self):
#         print("sir is second boos")
# class ishita_maam:
#     def main(self):
#         print("sir na ghar na main boos")
# class deepak_sir_sir_na_papa:
#     def main(self):
#         print("sir na papa")
# class priyal_maam_sir_na_mom:
#     def main(self):
#         print("this is sir na mummy")

# for obj in [priyal_maam_sir_na_mom(),deepak_sir_sir_na_papa(),ishita_maam(),tarang_sir()]:
#     obj.main()


# class Computer:
#     def on(self):
#         return "Start the computer"
# class moniter(Computer):
#     def on(self):
#         return "Shut_Down the computer"

# computer = [moniter(),Computer()]

# for computers in computer:
#     print(computers.on())


class yashmeet:
    def work(self):
        return "marva  nu kaam"
class meet(yashmeet):
    def work(self):
        return "maar khava nu kaam"
class yash(yashmeet):
    def work(self):
        return "vato kar va nu eb bija hare"
class hy_brid(meet,yash):
    def work(self):
        return "this is good frind only"

my_love_rekhali = [yashmeet(),meet(),yash(),hy_brid()]

for my_rekhali in my_love_rekhali:
    print(my_rekhali.work())