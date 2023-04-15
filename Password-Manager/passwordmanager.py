import hashlib

class PasswordManager:
    def __init__(self):
        self.passwords = {}
        
    def add_password(self, website, username, password):
        salt = "random_salt"  # Add your own random salt value here
        password_hash = hashlib.sha256((password + salt).encode()).hexdigest()
        self.passwords[website] = {'username': username, 'password_hash': password_hash}
        print("Password added successfully!")
        
    def remove_password(self, website):
        if website in self.passwords:
            del self.passwords[website]
            print("Password removed successfully!")
        else:
            print("Website not found in the password manager.")
            
    def display_passwords(self):
        print("Password Manager:")
        if self.passwords:
            for website, details in self.passwords.items():
                print("Website: {}\nUsername: {}\nPassword: ********".format(website, details['username']))
        else:
            print("No passwords found.")
            
    def check_password(self, website, password):
        salt = "random_salt"  # Add your own random salt value here
        password_hash = hashlib.sha256((password + salt).encode()).hexdigest()
        if website in self.passwords and self.passwords[website]['password_hash'] == password_hash:
            return True
        else:
            return False

def main():
    password_manager = PasswordManager()
    while True:
        print("\nMenu:")
        print("1. Add password")
        print("2. Remove password")
        print("3. Display passwords")
        print("4. Check password")
        print("5. Exit")
        choice = input("Enter your choice: ")
        
        if choice == "1":
            website = input("Enter website: ")
            username = input("Enter username: ")
            password = input("Enter password: ")
            password_manager.add_password(website, username, password)
        elif choice == "2":
            website = input("Enter website to remove: ")
            password_manager.remove_password(website)
        elif choice == "3":
            password_manager.display_passwords()
        elif choice == "4":
            website = input("Enter website to check password for: ")
            password = input("Enter password: ")
            if password_manager.check_password(website, password):
                print("Password is correct.")
            else:
                print("Password is incorrect.")
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == '__main__':
    main()

