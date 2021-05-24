class Account(object):
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, cash):
        self.balance += cash

    def transfer(self, amount):
        if self.balance < amount:
            raise BalanceError('Insufficient funds. Funds = {}'.format(self.balance))
        self.balance -= amount

class BalanceError(Exception):
    pass

if __name__ == "__main__" :
    account = Account(20)
    print(account.balance)
    account.deposit(20)
    print(account.balance)
    account.transfer(20)
    print(account.balance)
    account.transfer(30)
    print(account.balance)

