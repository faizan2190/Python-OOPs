# Practice Problem 1
# Create a class Point having two attributes x and y (the two coordinates of a point) and the 
# following methods:
#  setx(xcoord): sets the x coordinate of the point to xcoord
#  sety(ycoord): sets the y coordinate of the point to ycoord
#  get( ): returns the x and y coordinates of the Point type object as tuple (x , y)
#  move(dx, dy): changes the coordinates of the Point type object from the current position 
# (x , y) to (x+dx , y+dy)
class point:
    x = 0
    y = 0
    def setx(self, xcoord):
        self.x = xcoord
    def sety(self, ycoord):
        self.y = ycoord
    def get(self):
        return self.x, self.y
    def move(self, dx, dy):
        self.x += dx
        self.y += dy
p1=point( )
print(p1.get( ))
p1.setx(4)
p1.sety(7)
print(p1.get( ))
p1.move(1,1)
print(p1.get( ))

