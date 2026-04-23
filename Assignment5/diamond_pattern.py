#ask the user to enter an Odd number n.
# print a diamond shape made of stars with n as the widest row in the middle
#the upper half should expand from 1 star to n stars
#and the lower half should shrink back from n-2 stars to 1 star.
#using nested loops only

print("enter the odd value of n: ")
n=int(input())
i=1
j=int(n/2)+1
#print (j)
while(i<=n):
    if(i%2!=0):
        print(j*" ",i*"*")
        j=j-1
    i=i+1
k=n-1
l=2
while(k>=1):
    if(k%2!=0):
        print(l*" ",k*"*")
        l=l+1
    k=k-1

