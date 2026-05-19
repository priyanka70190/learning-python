"""Ask the user to enter n numbers.Find and print the second largest number in the list."""

print("Enter count :")
count = int(input())
print("Enter numbers: ")
string_numbers=input()
split_numbers=string_numbers.split(" ")
i=0
number_list=[]
while(i<len(split_numbers)):
    number_list.append(int(split_numbers[i]))
    i=i+1
print("List:",number_list)
sorted_list=[]
while(True):
 j=0
 max=number_list[0]
 while(j<len(number_list)):
    if(number_list[j]>max):
        max=number_list[j]
        j=j+1
    else:
        j=j+1
        continue
 if(j==len(number_list)):
    sorted_list.append(max)
    number_list.remove(max)
 if(len(number_list)==0):
     break
l=0
while(l<len(sorted_list)):
    if sorted_list[l-1]==sorted_list[l]:
            l=l+1
            if(l==len(sorted_list)):
              print("No Second Largest Number-All Elements are equal.")
            else:
               l=l+1
               continue

    else:
     print("Second Largest Number:",sorted_list[1])
     break