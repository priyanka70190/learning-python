"""Simulate a basic bank transaction system. Ask the user to enter the following:
   Account Type(Savings/Current)
   Current account balance
   Transaction Type(Deposit/Withdraw)
   Transaction Amount
 Apply the following rules :
 For Deposit :
   Amount must be greater than 0
   Maximum deposit allowed in one transaction is 10,000 $
   Add the amount to the balance and print the new balance
 For Withdrawl(Savings Account):
    Amount must be greater than 0
    cannot with draw more than current balance
    savings account must maintain a minimum balance of 500 $ at all times
    if the withdrawl wold bring the balance below 500 $,reject the transaction
For Withdrawl(Current Account):
    Amount must be greater than 0
    current account allows overdraft upto 200 $(balance can go down to -200$
    if the withdrawl exceeds balance +200$ ,reject the transaction
if the invalid account type or transaction type is entered,Print an error message.
    """

print("Enter Account Type(Savings/Current): ")
account_type=input()

print("Enter Current Balance: ")
account_balance=float(input())

print("Enter Transaction Type(Deposit/Withdraw): ")
transaction_type=input()

print("Enter Transaction Amount: ")
amount=float(input())

if(transaction_type=="Deposit"):
    if(amount>0 and amount<=10000):
        new_balance=account_balance+amount
        print("New Balance: ",new_balance)
    else:
        print("Transaction Rejected!")
        print("Maximum Deposit Limit per transaction is 10,000 $")
        print("Current Balance Remains: ",account_balance)
elif(transaction_type=="Withdraw" and account_type=="Savings" ):
        if(amount>0 and amount<=account_balance):
            new_balance=account_balance-amount
            if(new_balance<500):
                print("transaction rejected")
            else:
                print("Transaction Approved!")
                print("Amount Withdraw :",amount)
                print("New Balance: ",new_balance)
elif(transaction_type=="Withdraw" and account_type=="Current"):
    if(amount>0):
        new_balance=account_balance-amount
        if(new_balance>=-200):
            print("Transaction Approved!")
            print("Amount Withdraw :", amount)
            print("New Balance: ",new_balance)
        else:
            print("transaction rejected")
else:
    print("Invalid account type or transaction type is entered")