# Constructor
class Fraction:
    def __init__(self,x,y):
        self.numerator = x
        self.denominator = y
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
f1 = Fraction(33,100)
print("Autoinitialization",f1.getFraction())
f1.setNumerator(4)
f1.setDenominator(10)
print("From setter",f1.getFraction())
# # f2 = Fraction() #error
# for this condition of we Create a default constructor like
# def __init__(self,x=0,y=1)

# - del<object_name> can be used to forcefully destroy an object
