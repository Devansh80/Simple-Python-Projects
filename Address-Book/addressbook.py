class Contact:
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone
        
    def __str__(self):
        return "Name: {}\nEmail: {}\nPhone: {}".format(self.name, self.email, self.phone)

class AddressBook:
    def __init__(self):
        self.contacts = []
        
    def add_contact(self, contact):
        self.contacts.append(contact)
        print("Contact added successfully!")
        
    def remove_contact(self, name):
        for contact in self.contacts:
            if contact.name == name:
                self.contacts.remove(contact)
                print("Contact removed successfully!")
                return
        print("Contact not found in the address book.")
            
    def display_contacts(self):
        print("Address Book:")
        if self.contacts:
            for contact in self.contacts:
                print(contact)
        else:
            print("No contacts found.")
            
def main():
    address_book = AddressBook()
    while True:
        print("\nMenu:")
        print("1. Add contact")
        print("2. Remove contact")
        print("3. Display contacts")
        print("4. Exit")
        choice = input("Enter your choice: ")
        
        if choice == "1":
            name = input("Enter name: ")
            email = input("Enter email: ")
            phone = input("Enter phone: ")
            contact = Contact(name, email, phone)
            address_book.add_contact(contact)
        elif choice == "2":
            name = input("Enter name to remove: ")
            address_book.remove_contact(name)
        elif choice == "3":
            address_book.display_contacts()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == '__main__':
    main()

