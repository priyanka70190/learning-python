#Ask the user to enter starting and last number.
#print all the integers from starting number upto and including last number each on new line


print("enter Starting number: ")
start=int(input())
print("enter Last number: ")
last=int(input())
print("Series is: ")
i=start

while(i<=last):
    print(i)
    i=i+1
