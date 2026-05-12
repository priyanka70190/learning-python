"""Ask the user to enter 5 numbers.store them in a list
   print the sum and average of all numbers."""

print("enter 5 numbers:")
i=1
numbers=[]
while(i<=5):
    print("Enter number ",i,":")
    number=int(input())
    numbers.append(number)
    i=i+1
print("Numbers: ",numbers)
j=0
sum=0
while(j<5):
    sum=sum+numbers[j]
    j=j+1
print("Sum: ",sum)
average=sum/len(numbers)
print("Average: ",average)