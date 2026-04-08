from Bank.rbi_bank import RbiBank


class HdfcBankaccount(RbiBank):

    def __init__(self,balance):
        self._balance = balance

    def credit(self,amount):
        self._balance = self._balance +  amount

    def debit(self, amount):

       try:
        self.totalamount= amount+amount * .05
        if self._balance <= self.totalamount:
            raise Exception("Insufficient balance------------")
            print("Insufficient funds")
        else:
            self._balance -= amount
            self._balance -= amount * .05

       except Exception as e:  # Catching the exception
           print(f"Error: {e}")

    def get_balance(self):
        print("Elby's account balance is in hdfc bank", self._balance)
