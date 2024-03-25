# Write code to implement class Worker that supports two private attributes hoursWorked
# and wageRate, and the following public methods:
#  setHoursWorked(h): sets hoursWorked to h
#  changeRate(r): changes the worker’s pay rate to the new hourly rate r
#  pay(): returns the pay as product of hoursWorked and wageRate
class Worker:
    def setHoursWorked(self, h):
        self.__HoursWorked = h
    def changeWageRate(self, r):
        self.__wageRate = r
    def pay(self,):
        return self.__HoursWorked * self.WageRate