# class Book:
#     title = ""
#     author = ""
#     year = 0.0
#     is_check_out = False

#     def book_d(self):
#         print(f"My_book {self.title},{self.author},{self.year},{self.is_check_out}")

# my_book = Book()
# my_book.title = "S"
# my_book.author = "A"
# my_book.year = 1.2
# my_book.is_check_out = True

# my_book.book_d()


class Bank_Account:
    account_holder =""
    deposit = 0
    withdraw = 0
    balance = 0

    def Account(self):
        print(f"{self.account_holder},{self.balance}")

account_d = Bank_Account()

account_d.account_holder = "A"
account_d.deposit = 45000
account_d.withdraw = 10000
account_d.balance = 35000


account_d.Account()


