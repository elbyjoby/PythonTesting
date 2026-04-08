
class Society:

    def __init__(self,balance):
        self._balance = balance

    def creditw(self,amount):
        self._balance = self._balance +  amount

    def debitw(self, amount):

        self.totalamount= amount+amount * .05
        if self._balance <= self.totalamount:
            print("Insufficient funds")
        else:
            self._balance -= amount
            self._balance -= amount * .05

    def get_balancew(self):
        print("Elby's account balance is in Society bank", self._balance)
