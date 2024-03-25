# Define a class Animal with two attributes specie and language and following method:
#  speak ( ) – prints a message from the animal [e.g.: I am a cat and I meow]
class Animal:
    specie = "cat"
    language = "meow"
    def speak(self):
        print("I am "+self.specie+" and I can "+self.language)
obj1 = Animal()
print("attribute 1 is: " + obj1.specie)
print("attribute 1 is: " + obj1.language)
obj1.speak()

# Changing values of the attributes
# Method 1: Accessing class attributes from the main code

obj2 = Animal()
obj2.specie = "lion"
obj2.language = "roar"
print("attribute 1 is: " + obj2.specie)
print("attribute 1 is: " + obj2.language)
obj2.speak()
obj3 = Animal()
obj3.speak()

# Changing values of the attributes
# Method 2: Defining setter methods

class Animal1():
    specie = "cat"  
    language = "meow"
    def setSpecie(self, s):
        self.specie = s
    def setLanguage(self, l):
        self.language = l
    def speak(self):
        print("I am a",self.specie,"and I can",self.language)
obj4 = Animal1()
obj4.setSpecie("mouse")
obj4.setLanguage("squeak")
obj4.speak()

# Changing values of the attributes
# Method 3: Defining setter methods without defining class attributes explicitly
class Animal2:
    def setSpecie(self, s):
        self.specie = s
    def setLanguage(self,l):
        self.language = l
    def speak(self):
        print("I am a",self.specie,"and I can",self.language)
obj5 = Animal2()
# print(obj5.specie) #error
obj5.setSpecie("cat")
obj5.setLanguage("meow")
obj5.speak()
print(obj5.specie)

# Changing values of the attributes
# Let’s define getter methods too

class Animal3:
    def setspecie(self, s):
        self.specie = s
    def setlanguage(self, l):
        self.language = l
    def getspecie(self):
        return self.specie
    def getlanguage(self):
        return self.language
obj6 = Animal3()
# print(obj6.getspecie()) error 
obj6.setspecie("lion")
obj6.setlanguage("roar")
print(obj6.getspecie())
print(obj6.getlanguage())