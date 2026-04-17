""" Ask the user to enter the total bill amount.Apply a discount based on following criteria:
    bill above than 5000-->20% discount
    bill above 2000 -->10% discount
    bill above 1000-->5% discount
    bill 1000 or below -->no discount
    Print the discount amount and the final bill after discount"""
print("Enter Total Bill Amount: ")
bill_amnt=float(input())
if (bill_amnt > 5000):
    print("Discount is: 20 %")
    discount=20/100*bill_amnt
    print("Discount Amount is:",discount)
    print("Final Bill Amount is:",bill_amnt-discount)
elif (bill_amnt > 2000):
    print("Discount is: 10 %")
    discout=10/100*bill_amnt
    print("Discount Amount is:",discout)
    print("Final Bill Amount is:",bill_amnt-discout)
elif (bill_amnt > 1000):
    print("Discount is: 5 %")
    discout=5/100*bill_amnt
    print("Discount Amount is:",discout)
    print("Final Bill Amount is:",bill_amnt-discout)
else:
    print("no discount applicable.")


