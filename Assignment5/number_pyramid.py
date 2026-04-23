#Ask the user to enter a number n.Print a number pyramid pattern with n rows,
#where each row i prints numbers from 1 upto i,
#followed by numbers back down from i-1 to 1,using nested loops only

print("enter the number of rows: ")
rows=int(input())

i=1

while(i<=rows):
    j=1
    while(j<=i):
        print(j,end=" ")
        j+=1
    k=i-1
    while(k>=1):
        print(k,end=" ")
        k=k-1
    i+=1
    print()
