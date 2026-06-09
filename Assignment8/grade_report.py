"""Ask the user to enter their name and marks for 3 subjects.calculate the average
   and use an f-string to print a formatted report card showing each subject marks
   the average (round to 2 decimal places) and a pass/fail status
   pass if average>=50"""

print("Name:",end=" ")
name=input()
print("Marks for subject 1:",end=" ")
subject1=int(input())
print("Marks for subject 2:",end=" ")
subject2=int(input())
print("Marks for subject 3:",end=" ")
subject3=int(input())
average=(subject1+subject2+subject3)/3
print(f"----Report Card for {name}----")
print(f"subject1:{subject1} | subject2:{subject2} | subject3:{subject3}")
print(f"Average:{average:.2f}")
if average>=50:
  print("Status:Pass")
else:
    print("Status:Fail")