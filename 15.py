# A child class inherits all attributes and methods of the parent class
class Animal:
    def __init__(self, s="animal", l="talk"):
        self.specie = s
        self.language = l
    def info(self):
        print("Specie:",self.specie,"\nLanguage:",self.language)
    def speak(self):
        print("I am",self.specie,"and I can",self.language)
    

class Duck(Animal):
    # pass 
    def setBeakType(self, b='short'):
        self.beakType=b


tom = Animal("cat","meow")
# tom.setBeakType('long and curved') #error
tom.info()
tom.speak()

daffy = Duck("duck","quack")
daffy.setBeakType('long and curved')
daffy.info()
daffy.speak()