"""Write a recursive fn binary_search(arr,target,low,high)
   that searches for a target value in a sorted list
   retutn its index or -1 if not found.
   Ask the user to enter a list of sorted numbers and a target to search for"""



def binary_search(arr,target,low,high):
    if low>high:     #if target is not in the list
       return -1

    #find middle index
    mid=(low+high)//2

    #check if target is at the middle
    if arr[mid]==target:
        return mid
    elif target<arr[mid]:   #if target is smaller do left search
        return binary_search(arr,target,low,mid-1)
    else:
        return binary_search(arr,target,mid+1,high) #if target is greater do right search




print("enter sorted numbers",end=" ")
n=input()
string_numbers=n.split(" ")
i=0
number_list=[]
while i<len(string_numbers):
    number_list.append(int(string_numbers[i]))
    i=i+1
print(number_list)
print("enter target:",end=" ")
target=int(input())
result=binary_search(number_list,target,0,len(number_list)-1)
if result !=-1:
    print(f"element found at index {result} ",end=" ")
else:
    print(f"element not found",end=" ")
