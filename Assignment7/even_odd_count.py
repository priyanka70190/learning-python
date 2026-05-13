"""Ask the user to enter n numbers.store them in a list.
   count how many are even and how many are odd
   print both counts"""

print("Enter count:")
n=int(input())
print("Enter numbers:")
number=input()
string_numbers=number.split(" ")
numbers=[]
j=0
while j<len(string_numbers):
    numbers.append(int(string_numbers[j]))
    j=j+1
print("List:",numbers)
even=0
odd=0
i=0
even=0
odd=0
while i<len(numbers):
    if numbers[i]%2==0:
        even=even+1
    else:
        odd=odd+1
    i=i+1
print("Even count:",even)
print("Odd count:",odd)