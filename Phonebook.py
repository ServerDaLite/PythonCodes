# @ServerLite | Feb 13, 2023 | 1:33 PM
# Make a phonebook that stores contacts for users

# Creating the phonebook class
class Phonebook():
    def __init__(self):
        self.memory = dict()
    
    # Adds contact towards the phonebook
    def addContact(self, name, phone_number):
        self.memory[phone_number] = name
        
    # Edits the contact towards the phonebook
    def editContact(self, name, phone_number):
        for number in self.memory:
            if self.memory[number] == name:
                del self.memory[number]
                self.memory[phone_number] = name
                break
    
    # Removes the contact towards the phonebook
    def removeContact(self, name):
        for number in self.memory:
            if self.memory[number] == name:
                del self.memory[number]
                break
    
    # Shows the conatcs from within the phonebook
    def display(self):
        for number in self.memory:
            print(f"{number} ~ {self.memory[number]}")
        print("")
    
book1 = Phonebook()

book1.addContact("John Doe", "111-111-1111")
book1.addContact("Jane Doe", "222-222-2222")
book1.display()

book1.editContact("John Doe", "111-222-3333")
book1.display()

book1.removeContact("Jane Doe")
book1.display()
