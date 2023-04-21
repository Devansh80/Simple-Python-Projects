# Define a class named Account
class Account:
    # Define a constructor that initializes name, pin, balance and transaction history attributes
    def __init__(self, name, pin, balance):
        self.name = name
        self.pin = pin
        self.balance = balance
        self.transaction_history = []
    
    # Define a method named deposit that allows a user to deposit money    
    def deposit(self, amount):
        self.balance += amount
        self.transaction_history.append(f"Deposit: ${amount}")
        print(f"${amount} deposited. New balance: ${self.balance}")
    
    # Define a method named withdraw that allows a user to withdraw money    
    def withdraw(self, amount):
        # If the withdrawal amount is greater than the current balance, display an error message
        if amount > self.balance:
            print("Insufficient funds.")
        # If the withdrawal amount is greater than the maximum allowed limit, display an error message
        elif amount > 500:
            print("Withdrawal limit exceeded.")
        # Otherwise, deduct the withdrawal amount from the balance, add the transaction to the history, and display the updated balance
        else:
            self.balance -= amount
            self.transaction_history.append(f"Withdrawal: ${amount}")
            print(f"${amount} withdrawn. New balance: ${self.balance}")
    
    # Define a method named check_balance that displays the current balance
    def check_balance(self):
        print(f"Account balance: ${self.balance}")
    
    # Define a method named check_history that displays the transaction history    
    def check_history(self):
        print("Transaction history:")
        for transaction in self.transaction_history:
            print(transaction)

# Define a main function
def main():
    # Prompt the user for name, pin and balance to create an account object
    print("Welcome to the ATM.")
    name = input("Enter your name: ")
    pin = input("Enter your PIN: ")
    balance = int(input("Enter your starting balance: "))
    account = Account(name, pin, balance)
    
    # Display the menu of options until the user chooses to exit 
    while True:
        print("\n1. Deposit")
        print("2. Withdraw")
        print("3. Check balance")
        print("4. Check transaction history")
        print("5. Exit")
        choice = int(input("Enter your choice: "))
        
        # Call the appropriate method based on the user's choice
        if choice == 1:
            amount = int(input("Enter the amount to deposit: "))
            account.deposit(amount)
        elif choice == 2:
            amount = int(input("Enter the amount to withdraw: "))
            account.withdraw(amount)
        elif choice == 3:
            account.check_balance()
        elif choice == 4:
            account.check_history()
        elif choice == 5:
            print("Thank you for using the ATM.")
            break
        else:
            print("Invalid choice. Please try again.")
        
        # If the transaction history exceeds 5 transactions, end the loop and display a message
        if len(account.transaction_history) > 5:
            print("Withdrawal limit reached.")
            break

# Call the main function
if __name__ == "__main__":
    main()

