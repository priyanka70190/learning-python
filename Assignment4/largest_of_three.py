""" Ask the user to enter three numbers.save them in three variables.
    find and print the largest of three numbers handle case when 2 or all three numbers are equal."""
print("Enter first number:")
a=int(input())
print("Enter second number:")
b=int(input())
print("Enter third number:")
c=int(input())

if(a>b):
    if(a>c):
       print("greatest number is:",a)
    else:
       print("greatest number is: ",c)

elif(b>c):
    print("greatest number is:",b)
elif(a==b==c):
    print("All three numbers are equal")
else:
    print("greatest number is:",c)