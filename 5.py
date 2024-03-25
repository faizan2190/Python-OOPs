# Practice Problem 3
# Develop a class Circle having two attributes: radius and color. Define the following methods:
# - setter and getter methods for these attributes
# - circumference( ): returns circumference of the Circle type object
# - area( ): returns area of the Circle type object 
class circle:
    radius = 0
    color = None
    def setradius(self, r):
        self.radius = r
    def setcolor(self, c):
        self.color = c
    def getradius(self):
        return self.radius
    def getcolor(self):
        return self.color
    def circumference(self):
        return 2*3.14*self.radius
    def area(self):
        return 3.14*self.radius**2
obj = circle()
obj.setradius(2)
obj.setcolor("red")
print(obj.circumference())
print(obj.area())