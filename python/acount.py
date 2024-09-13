class BankAccount:
    account_holder = ""
    balance = 0.0

    def show_balance(self):
        print(f"Account Holder:{self.account_holder}, balance :${self.balance}")

account = BankAccount()

account.account_holder = "Meet"
account.balance = 15000.00

account.show_balance()