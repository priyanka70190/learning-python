"""Ask the user to enter a list of numbers seperated by space.
 store them in a set and print the unique numbers"""

print("Enter a list of numbers separated by space:")
n=input()
string_numbers=n.split(" ")
set_of_numbers=set()
i=0
while i<len(string_numbers):
    set_of_numbers.add(int(string_numbers[i]))
    i=i+1
print("Unique Numbers:" ,set_of_numbers)