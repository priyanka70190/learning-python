"""Ask the user to enter two numbers.
   Ask the user to choose an operation(+,-,*,/)
   perform the chosen operation and print the result
   if the user enters a invalid operator,print an error message
   also handle division by 0
   """
print("enter first number:")
a=int(input())
print("enter second number:")
b=int(input())
print("enter the operation(add,subtract,multiply,divide):")
operation=input()
if(operation=="add"):
    print("Addition is :",a+b)
elif(operation=="subtract"):
    print("Subtraction is :",a-b)
elif(operation=="multiply"):
    print("Multiplication is :",a*b)
elif(operation=="divide"):
    if(b==0):
        print("Division by 0 is undefined")
    else:
        print("Division is :",a/b)
else:
    print("Invalid operator.Please enter a valid operator")