# Define a class Contact with name, email and phone attributes
class Contact:
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone
   
    # Define a string representation of the Contact object.    
    def __str__(self):
        return "Name: {}\nEmail: {}\nPhone: {}".format(self.name, self.email, self.phone)

# Define a class AddressBook which contains a list of contacts
class AddressBook:
    def __init__(self):
        self.contacts = []
    
    # Add a contact to the address book    
    def add_contact(self, contact):
        self.contacts.append(contact)
        print("Contact added successfully!")
    
    # Remove a contact from the address book
    def remove_contact(self, name):
        for contact in self.contacts:
            if contact.name == name:
                self.contacts.remove(contact)
                print("Contact removed successfully!")
                return
        print("Contact not found in the address book.")
    
    # Display all contacts in the address book
    def display_contacts(self):
        print("Address Book:")
        if self.contacts:
            for contact in self.contacts:
                print(contact)
        else:
            print("No contacts found.")

# Define a main function that provides a user menu to interact with the AddressBook            
def main():
    # Create an instance of the AddressBook class
    address_book = AddressBook()
    while True:
        print("\nMenu:")
        print("1. Add contact")
        print("2. Remove contact")
        print("3. Display contacts")
        print("4. Exit")
        # Get user choice from the menu
        choice = input("Enter your choice: ")
        
        if choice == "1":
            # Get user input for a new contact and add it to the AddressBook
            name = input("Enter name: ")
            email = input("Enter email: ")
            phone = input("Enter phone: ")
            contact = Contact(name, email, phone)
            address_book.add_contact(contact)
        elif choice == "2":
            # Get user input for a contact name to remove and remove it from the AddressBook
            name = input("Enter name to remove: ")
            address_book.remove_contact(name)
        elif choice == "3":
            # Display all contacts in the AddressBook
            address_book.display_contacts()
        elif choice == "4":
            # Exit the program
            print("Goodbye!")
            break
        else:
            # Handle invalid user input
            print("Invalid choice. Please try again.")

# Call the main function
if __name__ == '__main__':
    main()

