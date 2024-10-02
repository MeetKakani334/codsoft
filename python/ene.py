class BankAccount:

    _blance = 0

    def deposite(self,amount):
        if amount>0:
            self._blance+=amount
            print(f"deposit:{amount}")
        else:
            print("deposit positive amount")
    def withdrae(self,amount):
        if 0<amount<=self._blance:
            self._blance-=amount
            print(f"withdrae:{amount}")
        else:
            print("invalid amount")
    def check_balnce(self):
       return self._blance


bank = BankAccount()
bank.deposite(int(input("deposite your blance")))
bank.withdrae(int(input("withdrae your blance")))

print(f"bankbalnce is {bank.check_balnce()}")


             