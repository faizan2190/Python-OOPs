# Practice Problem 2
# Create a class Student having three attributes:
#  - name: holds name of the student 
#  - roll: holds the roll number for the student
#  - marks: a list of marks for 3 quizzes
# Define the following methods:
#  - setter and getter methods for these three attributes
#  - getStudent( ): prints Student type object’s info in the following format:
#  Student name: <name>
#  Roll number: <roll>
#  Marks:
#  Quiz1: <marks[0]> 
#  Quiz2: <marks[1]> 
#  Quiz3: <marks[2]>
#  - avg( ): returns average of the 3 quiz scores set for a Student type object
class student:
    name = None
    roll = None
    marks = [0,0,0]
    def setname(self, n):
        self.name = n
    def setroll(self, r):
        self.roll = r
    def setmarks(self, m):
        self.marks = m
    def getname(self):
        return self.name
    def getroll(self):
        return self.roll
    def getmarks(self):
        return self.marks
    def getstudent(self):
        print("Student name :",self.name)
        print("Student roll :",self.roll)
        print("Marks:")
        print("Quiz1: ",self.marks[0])
        print("Quiz2: ",self.marks[1])
        print("Quiz3: ",self.marks[2])
    def average(self):
        return (self.marks[0]+self.marks[1]+self.marks[2])/3

obj = student()
obj.setname("faizan")
obj.setroll("CS-052")
obj.setmarks([30,20,10])
print(obj.getstudent())
print(obj.average())