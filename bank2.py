class SimpleBank:
    def __init__(self, name):
        self.name = name
        self.balance = 0
        print(f"Welcome {name}! Account created.")
    
    def deposit(self):
        amount = float(input("How much to deposit? $"))
        self.balance += amount
        print(f"Deposited ${amount}. New balance: ${self.balance}")
    
    def withdraw(self):
        amount = float(input("How much to withdraw? $"))
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew ${amount}. New balance: ${self.balance}")
        else:
            print("Not enough money!")
    
    def show_balance(self):
        print(f"Balance: ${self.balance}")

# Simple interactive version
x = input("Enter your name: ")
account = SimpleBank(x)

while True:
    print("\n1. Deposit\n2. Withdraw\n3. Check Balance\n4. Exit")
    choice = input("Choose option: ")
    
    if choice == '1':
        account.deposit()
    elif choice == '2':
        account.withdraw()
    elif choice == '3':
        account.show_balance()
    elif choice == '4':
        print("Goodbye!")
        break
    else:
        print("Invalid choice!") 