"""Define a class called Rectangle.
Add two attributes: length and width.
Add a method called area() that returns the area of the rectangle.
Now, create an object, set its dimensions, and print the area."""

class Rectangle:
    def __init__(self,length,width):
        self.length = length
        self.width = width
    def area(self):
        return self.length*self.width

object1  = Rectangle(5,3)
print("Area is :",object1.area())