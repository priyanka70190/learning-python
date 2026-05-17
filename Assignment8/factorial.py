"""Ask the user to enter a positive integer n.
   write a recursive fn factorial(n) that returns the factorial of n.
   print the result."""




def factorial(n):
    if n ==0:
        return 1
    else:
     fact=n*factorial(n-1)
     return fact






print("Enter a positive integer:")
n = int(input())
fact=factorial(n)
print(f"factorial of {n} = {fact}")