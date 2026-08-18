# Mini Project: Addis Bank Account System (Version 1)

class BankAccount:
    """Class representing an encapsulated bank account."""
    def __init__(self, account_number, owner: str, initial_deposit):
        self.account_number = account_number
        self.owner = owner
        self._balance = max(0.0, initial_deposit)

    @property
    def balance(self) -> float:
        return self._balance

    def deposit(self, amount: float) -> bool:
        if amount > 0:
            self._balance += amount
            print(f"Successfully deposited ${amount:.2f}.")
            return True
        print("Error: Deposit amount must be positive.")
        return False

    def withdraw(self, amount: float) -> bool:
        if amount <= 0:
            print("Error: Amount must be positive.")
            return False
        if amount <= self._balance:
            self._balance -= amount
            print(f"Successfully withdrew ${amount:.2f}.")
            return True
        print("Error: Insufficient funds.")
        return False

    def display_info(self):
        print(f"\n--- Account Information ---")
        print(f"Account Number : {self.account_number}")
        print(f"Account Owner  : {self.owner}")
        print(f"Current Balance: ${self._balance:.2f}\n")


class AddisBankSystem:
    """CLI Menu-driven program managing multiple accounts."""
    def __init__(self):
        self.accounts = {}  # account_number -> BankAccount object
        self.account_counter = 1001

    def create_account(self):
        owner = input("Enter account holder's name: ").strip()
        if not owner:
            print("Error: Name cannot be empty.")
            return

        try:
            initial_deposit = float(input("Enter initial deposit amount: "))
        except ValueError:
            print("Invalid input! Setting initial deposit to $0.00.")
            initial_deposit = 0.0

        acc_num = f"ADDIS-{self.account_counter}"
        self.account_counter += 1

        new_acc = BankAccount(acc_num, owner, initial_deposit)
        self.accounts[acc_num] = new_acc
        print(f"Account successfully created! Your Account Number is: {acc_num}")

    def get_account(self) -> BankAccount:
        acc_num = input("Enter your Account Number: ").strip()
        account = self.accounts.get(acc_num)
        if not account:
            print("Error: Account number not found.")
        return account


        

    def run(self):
        while True:
            print("\n==================================")
            print("     ADDIS BANK ACCOUNT SYSTEM    ")
            print("==================================")
            print("1. Create New Account")
            print("2. Deposit Money")
            print("3. Withdraw Money")
            print("4. Check Balance")
            print("5. View Account Info")
            print("6. Exit")
            
            choice = input("Select an option (1-6): ").strip()

            if choice == "1":
                self.create_account()
            elif choice == "2":
                acc = self.get_account()
                if acc:
                    try:
                        amt = float(input("Enter deposit amount: "))
                        acc.deposit(amt)
                    except ValueError:
                        print("Invalid numeric entry.")
            elif choice == "3":
                acc = self.get_account()
                if acc:
                    try:
                        amt = float(input("Enter withdrawal amount: "))
                        acc.withdraw(amt)
                    except ValueError:
                        print("Invalid numeric entry.")
            elif choice == "4":
                acc = self.get_account()
                if acc:
                    print(f"Current Balance: ${acc.balance:.2f}")
            elif choice == "5":
                acc = self.get_account()
                if acc:
                    acc.display_info()
            elif choice == "6":
                print("Thank you for using Addis Bank System. Goodbye!")
                break
            else:
                print("Invalid option. Please choose a number between 1 and 6.")


if __name__ == "__main__":
    bank_app = AddisBankSystem()
    bank_app.run()