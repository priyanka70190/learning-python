"""Ask the user to enter 8 numbers some repeated.store them in a list.
   print the list with duplicates removed.
   preserving the orignal order"""

print ("enter 8 numbers some repeated:")
string_numbers=input()
split_numbers=string_numbers.split(" ")
i=0
number_list=[]
while i<len(split_numbers):
    number_list.append(int(split_numbers[i]))
    i=i+1
print("Original List:",number_list)

unique_list=[]
j=0
while j<len(number_list):
    k=0
    while k<len(unique_list):
        if number_list[j]!=unique_list[k]:
            k=k+1
            continue
        else:
            break

    if(k==len(unique_list)):
        unique_list.append(number_list[j])
    j=j+1


print("Unique List:",unique_list)