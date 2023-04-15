class Account:
    def __init__(self, name, pin, balance):
        self.name = name
        self.pin = pin
        self.balance = balance
        self.transaction_history = []
        
    def deposit(self, amount):
        self.balance += amount
        self.transaction_history.append(f"Deposit: ${amount}")
        print(f"${amount} deposited. New balance: ${self.balance}")
        
    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds.")
        elif amount > 500:
            print("Withdrawal limit exceeded.")
        else:
            self.balance -= amount
            self.transaction_history.append(f"Withdrawal: ${amount}")
            print(f"${amount} withdrawn. New balance: ${self.balance}")
    
    def check_balance(self):
        print(f"Account balance: ${self.balance}")
        
    def check_history(self):
        print("Transaction history:")
        for transaction in self.transaction_history:
            print(transaction)


def main():
    print("Welcome to the ATM.")
    name = input("Enter your name: ")
    pin = input("Enter your PIN: ")
    balance = int(input("Enter your starting balance: "))
    account = Account(name, pin, balance)
    
    while True:
        print("\n1. Deposit")
        print("2. Withdraw")
        print("3. Check balance")
        print("4. Check transaction history")
        print("5. Exit")
        choice = int(input("Enter your choice: "))
        
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
        
        if len(account.transaction_history) > 5:
            print("Withdrawal limit reached.")
            break


if __name__ == "__main__":
    main()

