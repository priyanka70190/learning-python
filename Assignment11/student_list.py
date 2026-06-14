"""
Define a class called Employee.
Add attributes name and salary.
Create a list of 4 Employee objects.
Write a method called is_promoted() that returns True if performance rating is 90 or above,
otherwise False.
Loop through the list and print each Employee name and whether they are promoted or sustained.

"""

class Employee:
    def __init__(self, name, salary,performance_rating):
        self.name = name
        self.salary = salary
        self.performance_rating = performance_rating
    def is_promoted(self):
        if self.performance_rating >= 90:
            val=True
            return val
        else:
            val=False
            return val


employees=[Employee("Alice",1000,80),
           Employee("Bob",2000,90),
           Employee("Charlie",3000,85),
           Employee("David",4000,75)]

for employee in employees:
    if employee.is_promoted():
        print(employee.name,"-","Promoted")
    else:
        print(employee.name,"-","Sustained")


