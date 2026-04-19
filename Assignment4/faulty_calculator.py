"""Faulty Calculator
Design a calculator which will correctly solve all the problems except the
following ones:
45*3=5555,56+9=77,56/6=4
your program should take operator and the two numbers as input from the user
and then return the result.

"""

print("enter your first number")
num1=int(input())
print("enter your second number")
num2=int(input())
print("enter the operator")
op=input()
if((num1==45 and num2==3 and op=="*")):
    print("Result is: 5555")
elif((num1==56 and num2==9 and op=="+")):
    print("Result is: 77")
elif((num1==56 and num2==6 and op=="/")):
    print("Result is: 4")
elif (op=="*"):
    print("Result is : ",num1 * num2)
elif (op=="+"):
    print("Result is : ",num1 + num2)
elif (op=="-"):
    print("Result is : ",num1 - num2)
elif (op=="/"):
    print("Result is : ",num1 / num2)
elif (op=="%"):
    print("Result is : ",num1 % num2)
else:
    print("unexpected error")
