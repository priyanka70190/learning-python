#Ask the user to enter a number.
#print the multiplication table of that number from 1 to 10

print("enter number: ")
num=int(input())

i=1
while(i<=10):
    print(num, "*", i,"=",num*i)
    i+=1