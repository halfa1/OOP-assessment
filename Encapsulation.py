class BankAccount:
    def __init__(self,balance=0):
        self.__balance =balance

    def deposit(self,deposit_amount):
        if deposit_amount>0:

            self.__balance+=deposit_amount
            return f'You deposited: {deposit_amount} ,new balance is: {self.__balance}'
        else:
            return f'Money must be positive:'
    def withdraw(self,withdraw_amount):
        if 0<withdraw_amount<self.__balance:
            self.__balance-=withdraw_amount
            return f'You withdrew: {withdraw_amount},new balance: {self.__balance}'
        else:
            return f'You have insufficient funds'


account1 = BankAccount(1000)

print(account1.withdraw(500))
print(account1.deposit(200))

