# Implement a class Shape having one attribute noOfSides, which is set to 1 by default in the constructor. 
# From Shape derive a class Rectangle, having attributes length and width, supporting the following 
# methods:
#  perimeter(): returns the perimeter of the rectangle
#  area(): returns the area of the rectangle
#  Also define appropriate constructor setting both length and width to 0 by default and noOfSides
# to 1. 
# The object when printed should display the following:
# Sides: <number of sides>
# Length: <length>
# Width: <width>
# Perimeter: <perimeter of the rectangle>
# Area: <area of the rectangle>
# In the main program, input values for length and width of the rectangle from user, instantiate this rectangle and 
# print this object on screen.
class shape:
    def __init__(self,s=1):
        self.noOfSides = s
class rectangle(shape):
    def __init__(self,s,l=0,w=0):
        self.length = l
        self.width = w
        shape.__init__(self,s)
    def perimeter(self):
        return 2*(self.length+self.width)
    def area(self):
        return self.length*self.width
    def __str__(self):
        return (f"Sides: {self.noOfSides}\nLength: {self.length}\nWidth: {self.width}\nPerimeter: {self.perimeter()}\nArea: {self.area()}")



l = int(input("Enter the length of the rectangle"))
w = int(input("Enter the width of the rectangle"))
r = rectangle(4,l,w)
print(r)