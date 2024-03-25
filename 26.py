# A child class inherits attributes and methods from all the parents
class A:
    def methodA(self):
        print("In method A")
class B:
    def methodB(self):
        print("In method B")
class C(A, B):
    def methodC(self):
        print("In method C")

objC = C()
objC.methodC()
objC.methodB()
objC.methodA()
