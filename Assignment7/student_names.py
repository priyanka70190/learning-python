"""Ask the user to enter 5 student names one by one.
   store them in a list and print the complete list
   and print first student and the last student"""

print("enter 5 student names one by one:")
i=1
students=[]
while i<=5:
    print("Enter student name ",i,":")
    name=input()
    students.append(name)
    i=i+1
print("All students:",students)
print("First student:",students[0])
#print("Last student:",students[-1])
print("Last student:",students[len(students)-1])