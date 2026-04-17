""" Ask the user to enter marks out of 100.Print the grade based on following criteria:
    90 and above --> grade A
     75 to 89 --> grade B
      60 to 74 --> grade C
       40 to 59 --> grade D
       below 40 --> grade F"""

print("Enter marks out of 100 : ")
marks=int(input())

if(marks>=90):
    print("Congratulations... ! you got Grade A")
elif(marks>=75):
    print("Congratulations... ! you got Grade B")
elif(marks>=60):
    print("Congratulations... ! you got Grade C")
elif(marks>=40):
    print("Congratulations... ! you got Grade D")
else:
    print("sorry... ! you got Grade F")