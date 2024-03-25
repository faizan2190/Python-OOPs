# Write code to create a class called Time that has separate member data for hours, minutes, and 
# seconds. Make constructor to initialize these attributes, with 0 being the default value. Add the 
# following methods:
#  printTime(): displays time in 11:59:59 format
#  addTime(t): takes one argument t of Time type and adds this time to the current time 
# of the self object
# Instantiate two objects t1 and t2 to any arbitrary values, display both the objects, add t2 to 
# t1 and display the result.
class Time:
    def __init__(self, h=0, m=0, s=0):
        self.hour = h
        self.minutes = m
        self.seconds = s
    def printTime(self):
        # print(f'{self.hour }:{self.minutes }:{self.seconds}')
        print(f'{self.hour:02d}:{self.minutes:02d}:{self.seconds:02d}')
    def addTime(self,t):
        self.seconds+=t.seconds
        if self.seconds>=60:
            self.seconds-=60
            self.minutes+=1
        self.minutes+=t.minutes
        if self.minutes>=60:
            self.minutes-=60
            self.hour+=1
        self.hour+=t.hour
        if self.hour>=24:
            self.hour-=24
t1=Time(23,44,30)
t1.printTime()
t2=Time(2,4,30)
t2.printTime()
t1.addTime(t2)
t1.printTime()