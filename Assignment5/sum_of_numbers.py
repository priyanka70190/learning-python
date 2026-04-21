#Ask the user to enter starting and last number
#calculate and print the sum of all integers from starting number upto and including the last number


print("enter first number: ")
start=int(input())
print("enter last number: ")
last=int(input())

i=start
sum=0
while(i<=last):
    sum+=i
    i+=1
print("sum of numbers from",start,"to",last,"is: ",sum)