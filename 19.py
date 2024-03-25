# # Example 2: Overriding the method __init__

# # Approach 1: Initialize all instance variables in the child class's __init__
# # In this approach, the child class's __init__ method explicitly initializes all instance variables, including those inherited from the parent class.
# class Bird:
#     def __init__(self, species, language, beak_type):
#         self.species = species
#         self.language = language
#         self.beak_type = beak_type

# class Parrot(Bird):
#     def __init__(self, species, language, beak_type, color):
#         # Initializing all instance variables in Parrot's __init__
#         self.species = species
#         self.language = language
#         self.beak_type = beak_type
#         self.color = color

# # Creating an instance of Parrot
# p1 = Parrot("Parrot", "Squawk", "Hook", "Green")

# Approach 2: Initialize only beakType in the child class's __init__ and call parent class's __init__ for the remaining attributes

class Bird:
    def __init__(self, species, language, beak_type):
        self.species = species
        self.language = language
        self.beak_type = beak_type

class Parrot(Bird):
    def __init__(self, species, language, beak_type, color):
        # Calling parent class's __init__ to initialize common attributes
        Bird.__init__(self,species, language, beak_type)
        self.color = color

# Creating an instance of Parrot
p2 = Parrot("Parrot", "Squawk", "Hook", "Green")
