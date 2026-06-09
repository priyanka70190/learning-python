"""Ask the user to enter a positive integer.
write a recursive fn sum_digits(n)
that returns the sum of all its digits
print the result"""

def sum_digits(n):
    if n==0:
        return 0
    else:
       sum=(n%10)+sum_digits(n//10)
       return sum




print("enter a number",end=" ")
n=int(input())
sum= sum_digits(n)
print("sum of digits:",sum)
