"""Create  a class bank_account with methods deposit(amount) and withdraw(amount).
   Each method and the class itself must have a descriptive docstring.
   Add a method get_balance()that return the current balance.
   print all the docstring using __doc__ and demonstrate all theee methods
   with sample values."""

class bank_account:
    """class bank_account with methods deposit(amount) and withdraw(amount)."""
    def __init__(self,bankaccount):
        self.bankaccount=bankaccount



    def deposit(amount):
     """
    this method in class is used to deposit an amount into the bank_account
    """



    def withdraw(amount):
        """this method in class is used to withdraw an amount from the bank_account"""

    def get_balance():
         """this method in class is used to get the current balance of the bank_account"""



print(bank_account.__doc__)
print(bank_account.withdraw.__doc__)
print(bank_account.deposit.__doc__)
print(bank_account.get_balance.__doc__)