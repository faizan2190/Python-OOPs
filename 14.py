# Write code to create a class Tracker that includes a data member that holds a serial number for 
# each object created from the class. That is, the first object created will be numbered 1, the 
# second 2, and so on. 
# For this, create a class attribute named count; then, as each object is created, its constructor 
# can examine this count member variable to determine the appropriate serial number for the 
# new object. 
# Add a method that permits an object to report its own serial number. 
# Then write a main program that creates three objects and queries each one about its serial 
# number. They should respond I am object number 2, and so on.
class Tracker:
    count = 0
    def __init__(self):
        Tracker.count += 1
        self.serialNo = Tracker.count
    def reportSerial(self):
        print("I am",self.serialNo)
n1=Tracker()
n2=Tracker()
n3=Tracker()
n1.reportSerial()
n2.reportSerial()
n3.reportSerial()
print("Dictionary of n1:", n1.__dict__)