"""Write a fn calculate_area(length,width) that returns the area of a rectangle.
   Add a proper single line docstring to a fn.
   Then call the function and print both the result and fn docstring using __doc__ """

def calculate_area(length,width):
    """Return the area of rectangle given its length and width."""
    area=length*width
    return area
print("enter length:")
length=int(input())
print("enter width:")
width=int(input())
area=calculate_area(length,width)
print(calculate_area.__doc__)
print("Area:",area)