"""Ask the user to enter n numbers.
   store them in a list.
   print the list in revered order"""

print("Enter number count: ")
count=int(input())
numbers=[]
i=1
while i<=count:
    print("Enter the number",i,":")
    number=int(input())
    numbers.append(number)
    i=i+1
print("Original list: ",numbers)
reversed_numbers=[]

j=len(numbers)-1
while j>=0:
    reversed_numbers.append(numbers[j])
    j=j-1
print("Reversed list: ",reversed_numbers)