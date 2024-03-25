class fraction:
    def setNumerator(self, x):
        self.numerator = x
    def setDenominator(self, y):
        if y != 0:
            self.denominator = y
        else:
            print("setting y to 1")
            self.denominator = 1
    def getFraction(self):
        return self.numerator, self.denominator
    def convertToDecimal(self):
        return self.numerator/self.denominator
f1 = fraction()
f1.setNumerator(4)
f1.setDenominator(10)
print(f1.getFraction())
print(f1.convertToDecimal())

f2 = fraction()
f2.setDenominator(0)
f2.setNumerator(1)
print(f2.getFraction())

# Listing Class Attributes and Methods in Python
#  Running dir( ) function on any class (built-in or user-defined) shows all class attributes 
# and methods defined in a class

print(dir(fraction))