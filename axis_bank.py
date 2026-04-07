from rbi_bank import RbiBank

class AxisBankaccount(RbiBank):

    def __init__(self,balance):
        self._balance = balance

    def credit(self,amount):

        self._balance +=  amount

    def debit(self,amount):

        self.totalAmount = amount + amount * 0.1
        if self.totalAmount > self._balance:
            raise Exception("Insufficient balance")
            print("Insufficient funds")
        else:
            self._balance -= self.totalAmount


    def get_balance(self):
        print("Elby's account balance is in axis bank", self._balance)


