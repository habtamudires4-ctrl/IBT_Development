# ==========================================
# Mini Project: Addis Bank System (Version 2)
# ==========================================
from abc import ABC, abstractmethod

class Account(ABC):
    def __init__(self, account_number: str, owner: str, initial_deposit: float = 0.0):
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
        print("Deposit amount must be positive.")
        return False

    @abstractmethod
    def withdraw(self, amount: float) -> bool:
        pass

    @abstractmethod
    def show_statement(self):
        pass


class SavingsAccount(Account):
    def __init__(self, account_number: str, owner: str, initial_deposit: float = 0.0, interest_rate: float = 0.07):
        super().__init__(account_number, owner, initial_deposit)
        self.interest_rate = interest_rate

    def withdraw(self, amount: float) -> bool:
        if 0 < amount <= self._balance:
            self._balance -= amount
            print(f"Successfully withdrew ${amount:.2f}.")
            return True
        print("Withdrawal failed: Insufficient funds.")
        return False

    def apply_interest(self):
        interest = self._balance * self.interest_rate
        self._balance += interest
        print(f"[{self.account_number}] Applied interest: ${interest:.2f}. New Balance: ${self._balance:.2f}")

    def show_statement(self):
        print(f"[Savings] Acc: {self.account_number} | Owner: {self.owner:<10} | Balance: ${self._balance:<8.2f} | Interest Rate: {self.interest_rate * 100}%")


class CurrentAccount(Account):
    def __init__(self, account_number: str, owner: str, initial_deposit: float = 0.0, overdraft_limit: float = 1000.0):
        super().__init__(account_number, owner, initial_deposit)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount: float) -> bool:
        if amount > 0 and (self._balance - amount >= -self.overdraft_limit):
            self._balance -= amount
            print(f"Successfully withdrew ${amount:.2f}.")
            return True
        print("Withdrawal failed: Overdraft limit exceeded.")
        return False

    def show_statement(self):
        print(f"[Current] Acc: {self.account_number} | Owner: {self.owner:<10} | Balance: ${self._balance:<8.2f} | Overdraft Limit: ${self.overdraft_limit:.2f}")


class AddisBankSystemV2:
    def __init__(self):
        self.accounts = {}  # account_number -> Account instance
        self.counter = 2001

    def _generate_acc_num(self, prefix: str) -> str:
        num = f"ADDIS-{prefix}-{self.counter}"
        self.counter += 1
        return num

    def create_savings_account(self):
        owner = input("Enter account owner name: ").strip()
        try:
            deposit = float(input("Enter initial deposit: "))
        except ValueError:
            deposit = 0.0
        
        acc_num = self._generate_acc_num("SAV")
        acc = SavingsAccount(acc_num, owner, deposit)
        self.accounts[acc_num] = acc
        print(f"Savings Account created successfully! Account Number: {acc_num}")

    def create_current_account(self):
        owner = input("Enter account owner name: ").strip()
        try:
            deposit = float(input("Enter initial deposit: "))
        except ValueError:
            deposit = 0.0
        
        acc_num = self._generate_acc_num("CUR")
        acc = CurrentAccount(acc_num, owner, deposit)
        self.accounts[acc_num] = acc
        print(f"Current Account created successfully! Account Number: {acc_num}")

    def _find_account(self) -> Account:
        acc_num = input("Enter Account Number: ").strip()
        acc = self.accounts.get(acc_num)
        if not acc:
            print("Account not found.")
        return acc

    def deposit_money(self):
        acc = self._find_account()
        if acc:
            try:
                amt = float(input("Enter amount to deposit: "))
                acc.deposit(amt)
            except ValueError:
                print("Invalid input.")

    def withdraw_money(self):
        acc = self._find_account()
        if acc:
            try:
                amt = float(input("Enter amount to withdraw: "))
                acc.withdraw(amt)
            except ValueError:
                print("Invalid input.")

    def show_single_statement(self):
        acc = self._find_account()
        if acc:
            acc.show_statement()

    def apply_interest_to_all_savings(self):
        print("\n--- Applying Interest to All Savings Accounts ---")
        count = 0
        for acc in self.accounts.values():
            if isinstance(acc, SavingsAccount):
                acc.apply_interest()
                count += 1
        if count == 0:
            print("No Savings Accounts found.")

    def show_all_accounts(self):
        """Demonstrates Polymorphism by calling show_statement() on all account objects."""
        print("\n================ ALL BANK ACCOUNTS ================")
        if not self.accounts:
            print("No accounts registered in system.")
            return
        
        for acc in self.accounts.values():
            acc.show_statement()  # Polymorphic call
        print("===================================================\n")

    def run(self):
        while True:
            print("\n==============================================")
            print("     ADDIS BANK SYSTEM (VERSION 2 - OOP)      ")
            print("==============================================")
            print("1. Create Savings Account")
            print("2. Create Current Account")
            print("3. Deposit")
            print("4. Withdraw")
            print("5. Show Statement")
            print("6. Apply Interest to All Savings Accounts")
            print("7. Show All Accounts (Polymorphism)")
            print("8. Exit")
            
            choice = input("Select an option (1-8): ").strip()

            if choice == "1":
                self.create_savings_account()
            elif choice == "2":
                self.create_current_account()
            elif choice == "3":
                self.deposit_money()
            elif choice == "4":
                self.withdraw_money()
            elif choice == "5":
                self.show_single_statement()
            elif choice == "6":
                self.apply_interest_to_all_savings()
            elif choice == "7":
                self.show_all_accounts()
            elif choice == "8":
                print("Exiting Addis Bank System V2. Goodbye!")
                break
            else:
                print("Invalid choice. Select between 1 and 8.")


if __name__ == "__main__":
    app = AddisBankSystemV2()
    app.run()