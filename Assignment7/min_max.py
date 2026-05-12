"""Ask the user to enter n numbers
   store them in a list
   find the max and min values using the loop"""

print("Enter Count: ")
n=int(input())
numbers=[]
print("Enter numbers:")
number=input()

string_numbers=number.split(" ")
for num in string_numbers:
    numbers.append(int(num))

print("List:",numbers)

min=numbers[0]
i=1
while i<=len(numbers)-1:
    if min>numbers[i]:
        min=numbers[i]
    i=i+1
print("Min Value:",min)

max=numbers[0]
i=1
while i<=len(numbers)-1:
    if numbers[i]>max:
        max=numbers[i]
    i=i+1
print("Max Value:",max)