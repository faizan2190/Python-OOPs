# Example - Testing public attributes and methods

class testPublic:
    def setPublicAttribute(self, x):
        self.PublicAttribute = x
    def getPublicAttribute(self):
        return self.PublicAttribute
    def publicMethod(self):
        print("I am a public attribute")
public = testPublic()
public.setPublicAttribute(2)
print(public.getPublicAttribute())
public.PublicAttribute = 99
print(public.getPublicAttribute())
public.publicMethod()

# Example - Testing protected attributes and methods

class TestProtected:
    def setProtectedAttr(self, x):
        self._protectedAttr=x
    def getProtectedAttr(self):
        return self._protectedAttr
    def _protectedMethod(self):
        print('I am a protected method')
protected = TestProtected()
protected.setProtectedAttr(2)
print(protected.getProtectedAttr())
protected._protectedAttr = 99
print(protected.getProtectedAttr())
protected._protectedMethod()

# Example - Testing private attributes and methods 

class TestPrivate:
    def setPrivateAttribute(self, x):
        self.__privateAttribute = x
    def getPrivateAttribute(self):
        return self.__privateAttribute
    def __privateMethod(self):
        print("I am a private method")
p2=TestPrivate()
p2.setPrivateAttribute(44)
print(p2.getPrivateAttribute())
# print(p2.__privatetAttr) error
print(p2._TestPrivate__privateAttribute)
# p2.__privateMethod() error 
p2._TestPrivate__privateMethod()