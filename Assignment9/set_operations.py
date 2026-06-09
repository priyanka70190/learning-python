"""Ask the user to enter two groups of numbers aeprated by spaces(one group per line).print
   their union ,intersectionand difference(first minus second)"""


print("enter FIRST group of numbers:",end=" ")
n1=input()
ist_number_string=n1.split(" ")
set_of_ist_numbers=set()
i=0
while i<len(ist_number_string):
    set_of_ist_numbers.add(int(ist_number_string[i]))
    i=i+1
print("enter SECOND group of numbers:",end=" ")
n2=input()
iind_number_string=n2.split(" ")
set_of_second_numbers=set()
j=0
while j<len(iind_number_string):
    set_of_second_numbers.add(int(iind_number_string[j]))
    j=j+1
union_set=set_of_ist_numbers.union(set_of_second_numbers)
print("union set:",union_set)
intersection_set=set_of_ist_numbers.intersection(set_of_second_numbers)
print("intersection set:",intersection_set)
difference=set_of_ist_numbers.difference(set_of_second_numbers)
print("difference:",difference)