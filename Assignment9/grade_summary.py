"""Ask the user to enter names and grades for students until they type 'done' for the name.
   using Dictionary Methods,print:
   All student names
   the average grade
   the highest scoring student
   the lowest scoring student"""
students={}
while True:
    print("Enter name (or 'done'):")
    name = input()
    if name == "done":
        break
    else:
        print("Grade:")
        grade = int(input())

    students[name]=grade

print("students:",students.keys())
print("higest Scorer:",max(students, key=students.get),"(",max(students.values()),")")
print("lowest Scorer:",min(students, key=students.get),"(",min(students.values()),")")

Average=sum(students.values())/len(students)
print("Average Grade:",round(Average,2))