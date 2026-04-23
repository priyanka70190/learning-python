#Ask the user to enter a number n.
#Print the first n terms of the fibonacci series.Where each term is the sum of 2 preceding terms.
#starting from 0 and 1

print("Enter number of terms: ")
n=int(input())
i=0
sum=0
list1=[0,1]
while (i<n):
   print(list1[i],end=" ")
   i=i+1
   if(i>=2):
      sum=list1[i-1]+list1[i-2]
      list1.append(sum)

