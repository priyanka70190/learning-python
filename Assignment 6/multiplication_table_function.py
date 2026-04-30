"""PROBLEM STATEMENT: Create a function called print_table() that takes a number as an argument.
 Inside the function, use a loop to print the multiplication table of that number up to 10.
 Ask the user to enter a number and call the function.
Commit the changes of the file and Push to GitHub."""


def print_table(number):
    i=1
    while(i<=10):
        print(number," * ",i," = ",number*i)
        i=i+1

print("Enter a number: ")
number=int(input())
print_table(number)




