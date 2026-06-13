"""
Define a class called Student.
Add three attributes: name, date of birth, and grade.
Create 4 objects of this class, assign values to the attributes, and print them.

"""

class Student:
    def __init__(self,name,age,grade):
        self.name = name
        self.age = age
        self.grade = grade
    def __str__(self):
        #return print("Name: ",self.name ,"\nAge: ",self.age,"\nGrade: ",self.grade)
        return f"Name: {self.name}\nAge: {self.age}\nGrade: {self.grade}"


s1=Student("Alice",20,"A")
s2=Student("Bob",25,"B")
s3=Student("Charlie",30,"C")
s4=Student("David",35,"D")
print(s1)
print(s2)
print(s3)
print(s4)

