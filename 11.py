# Revisiting the Point class 
# Create a class Point having two attributes x and y (the two coordinates of a point) and the 
# following methods:
#  setx(xcoord): sets the x coordinate of the point to xcoord
#  sety(ycoord): sets the y coordinate of the point to ycoord
#  get( ): returns the x and y coordinates of the Point type object as tuple (x , y)
#  move(dx, dy): changes the coordinates of the Point type object from the current position (x , 
# y) to (x+dx , y+dy) 


# __dict__ attribute to keep tract of instance variables

class Point:
    def __init__(self, xcoord=0 ,ycoord=0):
        self.x = xcoord
        self.y = ycoord
    def setx(self,xcoord):
        self.x = xcoord
    def sety(self,ycoord):
        self.y = ycoord
    def get(self):
        return self.x, self.y
    def move(self, dx, dy):
        self.x += dx
        self.y += dy
p1=Point(1,5)
print(p1.get( ))
print(p1.__dict__)
p1.setx(4)
p1.sety(7)
print(p1.get( ))
p1.move(1,1)
print(p1.get( ))
print(p1.__dict__)

# Macking attributes private  
class point:
    def __init__(self,xcoord=0,ycoord=0):
        self.__x=xcoord
        self.__y=ycoord
    def setx(self,xcoord):
        self.__x=xcoord
    def sety(self,ycoord):
        self.__y=ycoord
    def get(self):
        return self.__x, self.__y
    def move(self, dx, dy):
        self.__x+=dx
        self.__y+=dy
p=point()
print(p.get( ))
print(p.__dict__)