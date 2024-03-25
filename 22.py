#  The object is to create a phonebook to keep track of my contacts
# Thought Process
#  What data item I need to store?
#  - Name
#  - Phone numbers
#  - Email
#  What operation I need to perform on my data?
#  - add items to the phonebook
#  - print all entries of the phonebook
#  - sort entries in my phonebook by name
#  - search an item based on name (first or last)

class phoneBook:
    def __init__(self):
        self.contact =[]
    # adding contacts
    def addContact(self,name,email,contect):
        self.contact.append([name,email,contect])
    # printing the phonebook
    def __str__(self):
        string = "Name, Email, Phone No \n"
        for item in self.contact:
            string += item[0]+', '+item[1]+', '+item[2]+'\n'
        return string
    # sorting the contect name wise
    def sortContacts(self):
        self.contact.sort()
    # Why we need to build this as we have builtin methof sort within the method

Book1=phoneBook()
Book1.addContact('Maria Waqas','mariaw@neduet.edu.pk','111')
Book1.addContact('Ibshar Ishrat','ibshar@neduet.edu.pk','222')
print(Book1)
Book1.sortContacts()
print(Book1)
