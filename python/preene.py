from curses import longname


class BankAccount:
    balnce = 0
    _loan = 0

    def gpay(self,amount):
        if amount>=0:
            self.balnce+=amount
            print(f"deposit:{amount}")
        else:
            print("deposit positive amount")
    def transfer(self,amount):
        if 0<self._loan<=amount:

            print(f"transfer:{amount}")
        else:
            print("invalid amount")



    def paytm(self,amount):
        if amount>=0:
            self.balnce+=amount
            print(f"deposit:{amount}")
        else:
            print("deposit positive amount")
    def transfer(self,amount):
        if 0<amount<=self._loan:
            self.balnce-=amount
            print(f"transfer:{amount}")
        else:
            print("invalid amount")


    
    def phonepay(self,amount):
        if amount>=0:
            self.balnce+=amount
            print(f"deposit:{amount}")
        else:
            print("deposit positive amount")
    def transfer(self,amount):
        if 0<amount<=self.balnce:
            self.balnce-=amount
            print(f"transfer:{amount}")
        else:
            print("invalid amount")

    def loone(self):
        if 0<self._loan<=2000 and self.balnce <= 0:
            self.balnce -= self._loan
            self.balnce += self._loan
            print(f"lone:{self._loan}")
        else:
            print("invalid")
        return self._loan
    
bank = BankAccount()
bank.gpay(12500)
bank.transfer(1000)

