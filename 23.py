class PhoneBook(list):
 #Adding contacts
 #The append method of list will work
 #Printing the phonebook
 #object will be printed as a two dimensional list 
#  For pretty printing
    def __str__(self):
        strg='Name,Phone No., Email\n'
        for item in self:
            strg+=item[0]+', '+item[1]+', '+item[2]+'\n'
        return strg

        #Sorting the phonebook name-wise
 #sort method of list will work
 #Searching a contact by first or last name
    def search(self,name):
        # contactsFound=PhoneBook()
        contactsFound=list()
        for item in self:
            if name in item[0]:
                contactsFound.append(item)
        return contactsFound

Book1=PhoneBook()
Book1.append(['Maria Waqas','111','mariaw@neduet.edu.pk'])
Book1.append(['Ibshar Ishrat','222','ibshar@neduet.edu.pk'])
print(Book1)
Book1.sort()
print(Book1)
print(Book1.search('Maria'))