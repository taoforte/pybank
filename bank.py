class BankAccount:
    def __init__(self, owner_name, starting_balance=0):
        self.owner = owner_name
        self.balance = starting_balance
        self.transaction_history = []
        print(f"✅ Account created for {self.owner} with ${starting_balance}")
    
    def deposit(self, amount):
        """Add money to the account"""
        if amount > 0:
            self.balance += amount
            self.transaction_history.append(f"Deposited: ${amount}")
            print(f"💰 Deposited ${amount}. New balance: ${self.balance}")
        else:
            print("❌ Deposit amount must be positive!")
    
    def withdraw(self, amount):
        """Take money out of the account"""
        if amount <= 0:
            print("❌ Withdrawal amount must be positive!")
        elif amount <= self.balance:
            self.balance -= amount
            self.transaction_history.append(f"Withdrew: ${amount}")
            print(f"💸 Withdrew ${amount}. New balance: ${self.balance}")
        else:
            print(f"❌ Sorry, not enough money! Balance: ${self.balance}")
    
    def check_balance(self):
        """See how much money is in the account"""
        print(f"🏦 {self.owner}'s balance: ${self.balance}")
        return self.balance
    
    def show_transaction_history(self):
        """Show all transactions"""
        if self.transaction_history:
            print(f"\n📋 {self.owner}'s Transaction History:")
            for i, transaction in enumerate(self.transaction_history, 1):
                print(f"   {i}. {transaction}")
        else:
            print(f"\nNo transactions yet for {self.owner}")
    
    def transfer(self, amount, other_account):
        """Transfer money to another account"""
        if amount <= 0:
            print("❌ Transfer amount must be positive!")
        elif amount <= self.balance:
            self.balance -= amount
            other_account.balance += amount
            self.transaction_history.append(f"Transferred ${amount} to {other_account.owner}")
            other_account.transaction_history.append(f"Received ${amount} from {self.owner}")
            print(f"🔄 Transferred ${amount} to {other_account.owner}")
            print(f"   Your new balance: ${self.balance}")
        else:
            print(f"❌ Not enough money for transfer! Balance: ${self.balance}")

def create_account():
    """Helper function to create a new account"""
    print("\n" + "="*40)
    name = input("Enter account holder's name: ").strip()
    while not name:
        name = input("Please enter a valid name: ").strip()
    
    try:
        starting_balance = float(input("Enter starting balance (default 0): $") or 0)
        if starting_balance < 0:
            print("❌ Starting balance cannot be negative! Setting to $0")
            starting_balance = 0
    except ValueError:
        print("❌ Invalid amount! Setting starting balance to $0")
        starting_balance = 0
    
    return BankAccount(name, starting_balance)

def show_menu(account):
    """Display the main menu"""
    print(f"\n{'='*50}")
    print(f"🏦 WELCOME TO SIMPLE BANK - {account.owner}'s Account")
    print(f"{'='*50}")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. View Transaction History")
    print("5. Transfer Money")
    print("6. Switch Account")
    print("7. Create New Account")
    print("8. Exit")
    print("-"*50)

def bank_operations(account, all_accounts):
    """Handle all banking operations"""
    while True:
        show_menu(account)
        
        try:
            choice = input("\nEnter your choice (1-8): ").strip()
            
            if choice == '1':
                account.check_balance()
                
            elif choice == '2':
                try:
                    amount = float(input("Enter deposit amount: $"))
                    account.deposit(amount)
                except ValueError:
                    print("❌ Please enter a valid number!")
                    
            elif choice == '3':
                try:
                    amount = float(input("Enter withdrawal amount: $"))
                    account.withdraw(amount)
                except ValueError:
                    print("❌ Please enter a valid number!")
                    
            elif choice == '4':
                account.show_transaction_history()
                
            elif choice == '5':
                if len(all_accounts) < 2:
                    print("❌ Need at least 2 accounts to transfer money!")
                    continue
                    
                print("\nAvailable accounts:")
                for i, acc in enumerate(all_accounts):
                    if acc != account:
                        print(f"   {i}. {acc.owner} (Balance: ${acc.balance})")
                
                try:
                    acc_choice = int(input("Select account number to transfer to: "))
                    if 0 <= acc_choice < len(all_accounts) and all_accounts[acc_choice] != account:
                        target_account = all_accounts[acc_choice]
                        amount = float(input("Enter transfer amount: $"))
                        account.transfer(amount, target_account)
                    else:
                        print("❌ Invalid account selection!")
                except (ValueError, IndexError):
                    print("❌ Please enter a valid account number!")
                    
            elif choice == '6':
                if len(all_accounts) < 2:
                    print("❌ Only one account exists. Create another account first!")
                    continue
                    
                print("\nAvailable accounts:")
                for i, acc in enumerate(all_accounts):
                    print(f"   {i}. {acc.owner} (Balance: ${acc.balance})")
                
                try:
                    acc_choice = int(input("Select account number to switch to: "))
                    if 0 <= acc_choice < len(all_accounts):
                        return all_accounts[acc_choice]  # Return the new current account
                    else:
                        print("❌ Invalid account selection!")
                except ValueError:
                    print("❌ Please enter a valid number!")
                    
            elif choice == '7':
                new_account = create_account()
                all_accounts.append(new_account)
                print(f"✅ Created new account for {new_account.owner}")
                return new_account  # Switch to the new account
                
            elif choice == '8':
                print("\n💼 Thank you for using Simple Bank!")
                print("👋 Have a great day!")
                return None  # Signal to exit
                
            else:
                print("❌ Invalid choice! Please enter a number between 1-8")
                
        except KeyboardInterrupt:
            print("\n\n⚠️  Program interrupted. Exiting...")
            return None

def main():
    """Main function to run the banking system"""
    print("🏦 WELCOME TO SIMPLE BANK SYSTEM 🏦")
    print("Let's create your first account!")
    
    # Create first account
    all_accounts = []
    current_account = create_account()
    all_accounts.append(current_account)
    
    # Main banking loop
    while current_account is not None:
        current_account = bank_operations(current_account, all_accounts)
    
    # Show final summary
    if all_accounts:
        print("\n📊 FINAL ACCOUNT SUMMARY:")
        print("-" * 30)
        for account in all_accounts:
            print(f"{account.owner}: ${account.balance}")
        print(f"Total across all accounts: ${sum(acc.balance for acc in all_accounts)}")

# Run the program
if __name__ == "__main__":
    main()