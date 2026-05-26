"""Ask the user to enter two groups of numbers.print their symmetric difference
   (elements in either set but not in both).
   Also tell the user how many elements are exclusive to each group"""

print("Enter ist set of numbers:")
n=input()
string_numbers=n.split(" ")
numbers=set()
i=0
while i<len(string_numbers):
    numbers.add(int(string_numbers[i]))
    i+=1
print("Enter IInd set of numbers:")
n1=input()
string_numbers=n1.split(" ")
numbers1=set()
j=0
while j<len(string_numbers):
    numbers1.add(int(string_numbers[j]))
    j+=1
symmetric_difference=numbers.symmetric_difference(numbers1)

print("Symmetric Difference:",symmetric_difference)

intersection_set=numbers.intersection(numbers1)
#print("Intersection:",intersection_set)
print("Exclusive to first Group:",len(numbers)-len(intersection_set))
print("Exlusive to second Group:",len(numbers1)-len(intersection_set))
