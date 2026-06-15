class Student:
    def __init__(self,name):
        self.name=name
try:
    student=Student("Alex")
    print(student.age)
except AttributeError as e:
    print("AttributeError: ",e)

