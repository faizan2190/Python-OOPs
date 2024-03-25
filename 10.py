class Fraction:
    def __init__(self,x=0,y=1):
        self.numerator = x
        self.denominator = y
    def __del__(self):
        print("Good Bye everyone :(")
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
f1 = Fraction()
# - __del__ is the dunder method called when object is destroyed
print(f1.getFraction())
del f1
# print(f1.getFraction()) #error

