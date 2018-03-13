
class BankAccount():

    def __init__(self,balance=2000):
        self.balance=balance
    
    def deposit(self,amount):
        self.balance +=amount
        return self.balance

    def withdraw(self,amount):
        if self.balance>=amount:
            self.balance-=amount
        else:
            return "invalid transaction!"


class MininmuBalanceAccount(BankAccount):
   
    def __init__(self,balance=1000):
        pass
        



