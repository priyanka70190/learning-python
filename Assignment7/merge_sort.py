"""Ask the user to enter 4 numbers for list A and 4 numbers for list B
   merge them into one list,sort it in ascending order,print the result
   """

print("Enter 4 numbers for list A:")
string1=input()
string1_numbers=string1.split(" ")
i=0
numbers1=[]
while i<len(string1_numbers):
    numbers1.append(int(string1_numbers[i]))
    i=i+1
print("List A:",numbers1)

print("Enter 4 numbers for list B:")
string2=input()
string2_numbers=string2.split(" ")
j=0
numbers2=[]
while j<len(string2_numbers):
    numbers2.append(int(string2_numbers[j]))
    j=j+1
print("List B:",numbers2)

merged_list=[]
merged_sorted_list=[]
k=0
while k<len(numbers1):
    merged_list.append(numbers1[k])
    merged_list.append(numbers2[k])
    k=k+1
print("merged_list:",merged_list)
while(True):
 l=0
 min=merged_list[l]
 while l<len(merged_list):
   if min>merged_list[l]:
        min=merged_list[l]
   l=l+1
 merged_list.remove(min)
 #print(min)]
 merged_sorted_list.append(min)
 if(len(merged_list)==0):
   break

#print(merged_list)
print("merged_sorted_list:",merged_sorted_list)