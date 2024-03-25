# Example: User Documentation
class Animal:
    '''This is a Animal class having two attiribures'''
    def setSpecie(self, s):
        '''This is the setter method'''
        self.specie = s

print(help(Animal))
print(help(setSpecie()))