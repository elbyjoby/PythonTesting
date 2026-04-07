from abc import ABC, abstractmethod


class RbiBank(ABC):

    @abstractmethod

    def __init__(self,balance):
        pass

    @abstractmethod
    def credit(self,amount):
        pass

    @abstractmethod
    def debit(self,amount):
        pass

    @abstractmethod
    def get_balance(self):
        pass



