"""
PROBLEM STATEMENT:
Define a class called BankAccount.
Add an attribute balance.
Add a function : deposit(amount) to add money,
Add another function: withdraw(amount) to deduct money.
If the withdrawal amount is greater than the balance, raise a custom error InsufficientFundsError.
Print the balance after each operation"""

class BankAccount:
    def __init__(self,balance):
        self.balance = balance
    def deposit(self,amount):
        self.balance += amount
        print("Balance after deposit is:",self.balance)
    def withdraw(self,amount):
        if amount > self.balance:
            print("Insufficient Funds")
        elif amount < 0:
            print("you have entered amount that is less than 0")
        else:
          self.balance -= amount
          print("Balance after withdraw is:",self.balance)

obj = BankAccount(0)
obj.deposit(1000)
obj.withdraw(400)

