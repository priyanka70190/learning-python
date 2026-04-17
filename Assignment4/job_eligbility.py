""" A company is hiring candidates based on multiple eligbility criteria.
    Ask the user to enter the following details:
    Age
    Minimum Qualification(options:High school/bachelors/Masters)
    year of experience
    whether they have a valid certification(yes/no)

  Apply the following rules to determine which job role they qualify for:
  Senior Engineer --> Age 25 or above,Master degree,3+year experience,has certification
  Junior Engineer --> Age 21 or above,Bachelors Degree,1+year experience,has certification
  Trainee --> Age 18 or above,High School Qualification,any experience,no certification
  if none of the above ---> Print"Not eligible for any role at this time"
  check from the highest role downward.
  print the first role the candidate qualifies for
    """

print("Enter your age:")
age=int(input())
print("Enter Qualification(High School/Bachelors/Masters):")
qualification=input()
print("Enter years of experience:")
experience=int(input())
print("Do you have a certification(yes/No):")
certification=input()

qual_list=["Masters","Bachelors","High School"]
if(age>=25 and qualification=="Masters" and experience>=3 and certification=="Yes"):
    print("Congratulations! You are eligible for: Senior Engineer")
elif(age>=21 and qualification=="Bachelors" and experience>=1 and certification=="Yes"):
    print("Congratulations! You are eligible for: Junior Engineer")
elif(age>=18 and (qualification in qual_list)  and experience>=0 and (certification=="No" or certification=="Yes")):
    print("Congratulations! You are eligible for: Trainee Role")
else:
    print("Not eligible for any role at this time")
