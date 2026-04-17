""" Ask the user to enter their weight in kg
    Ask the user to enter their height in meters
    calculate the BMI using the formula :
    BMI=weight/(height*height)
    classify the BMI into the following categories and print the result:
     BMI below 18.5--->Underweight
     BMI 18.5 to 24.9 --> normal weight
     BMI 25 to 29.9 --> overweight
     BMI 30 and above --> obese"""


print("Enter your weight in kg: ")
weight=float(input())
print("Enter your height in meters: ")
height=float(input())
bmi=weight/(height*height)
print("Your BMI is: ",round(bmi,2))
if(bmi>=30):
    print("Category: Obese")
elif(bmi>=25):
    print("Category: Overweight")
elif(bmi>=18.5):
    print("Category: Normal Weight")
else:
    print("Category: Underweight")
