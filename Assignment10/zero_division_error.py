from sys import exception

try:
    x=10/0
    print(x)
except ZeroDivisionError:
    print("Zero Division Error Occured: division by 0 is not possible because its undefined in maths")