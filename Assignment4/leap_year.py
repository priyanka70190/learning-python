""" Ask the user to enter a year.
     check if the year is leap year or not using following rules:
     divisible by 4 -->leap year
     divisible by 100 --> not a leap year
     divisible by 400 --> leap year"""

print("enter a year: ")
year=int(input())

if(year%100==0):
    if(year%400==0):
        print("leap year")
    else:
        print("not a leap year")
else:
    if(year%4==0):
        print("Leap Year")
    else:
        print("Not a Leap Year")
