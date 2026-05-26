"""Ask the user to enter names and grades for 3 students.Store them in a dictionary.
   Print each students' name and grade using a loop
"""
dict1 = {}
i=1
while i<=3:

    print("Enter Student Name:")
    name=input()
    print("Enter Student Grade:")
    grade=int(input())
    dict1[name]=grade
    i=i+1
for name, grade in dict1.items():
    print(name,":",grade)

