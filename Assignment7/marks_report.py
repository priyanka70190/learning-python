"""store information for 3 students as tuples: name,Marks
   print each student's name,marks,grade(A>=80,B>=60,C>=40,F otherwise)
   """
students=(("Alice",92),("Bob",55),("Carol",38))
print(students)
i=0
while i<len(students):
    if students[i][1]>=80:
        grade="A"
    elif students[i][1]>=60:
        grade="B"
    elif students[i][1]>=40:
        grade="C"
    else:
        grade="F"
    print(students[i][0]," | ",students[i][1]," | Grade:",grade)
    i=i+1
