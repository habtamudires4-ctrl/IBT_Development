# ==========================================
# Level 2: Intermediate OOP Exercises
# ==========================================
from abc import ABC, abstractmethod

# 6. Abstract Base Class Definition
class Account(ABC):
    def __init__(self, owner: str, balance: float = 0.0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount: float):
        if amount > 0:
            self.balance += amount
            print(f"[{self.owner}] Deposited ${amount:.2f}. New Balance: ${self.balance:.2f}")

    def withdraw(self, amount: float):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"[{self.owner}] Withdrew ${amount:.2f}. New Balance: ${self.balance:.2f}")
        else:
            print(f"[{self.owner}] Insufficient funds.")

    def statement(self):
        """Base statement method to be overridden by subclasses."""
        print(f"Account Owner: {self.owner} | Balance: ${self.balance:.2f}")

    @abstractmethod
    def calculate_interest(self) -> float:
        """Abstract method that must be implemented by subclasses."""
        pass


# 4. SavingsAccount with Overridden statement() & Abstract Method
class SavingsAccount(Account):
    def __init__(self, owner: str, balance: float = 0.0, interest_rate: float = 0.05):
        super().__init__(owner, balance)
        self.interest_rate = interest_rate

    def statement(self):
        """Overrides statement() to show interest rate details."""
        print(f"[Savings Account] Owner: {self.owner} | Balance: ${self.balance:.2f} | Interest Rate: {self.interest_rate * 100}%")

    def calculate_interest(self) -> float:
        """Implements abstract method."""
        return self.balance * self.interest_rate


# 4. CurrentAccount with Overridden statement() & Abstract Method
class CurrentAccount(Account):
    def __init__(self, owner: str, balance: float = 0.0, overdraft_limit: float = 500.0):
        super().__init__(owner, balance)
        self.overdraft_limit = overdraft_limit

    def statement(self):
        """Overrides statement() to show overdraft limit details."""
        print(f"[Current Account] Owner: {self.owner} | Balance: ${self.balance:.2f} | Overdraft Limit: ${self.overdraft_limit:.2f}")

    def withdraw(self, amount: float):
        if self.balance - amount >= -self.overdraft_limit:
            self.balance -= amount
            print(f"[{self.owner}] Withdrew ${amount:.2f}. Balance: ${self.balance:.2f}")
        else:
            print(f"[{self.owner}] Exceeds overdraft limit.")

    def calculate_interest(self) -> float:
        """Current accounts do not yield interest."""
        return 0.0


# --- Testing Level 2 ---
if __name__ == "__main__":
    # 5. Polymorphism Practice
    print("--- 5. Polymorphism Demonstration ---")
    accounts: list[Account] = [
        SavingsAccount("Habtamu", 1500.0, 0.04),
        CurrentAccount("Abebe", 300.0, 200.0),
        SavingsAccount("Chala", 5000.0, 0.06)
    ]

    for acc in accounts:
        # Calling overridden statement() and deposit() polymorphically
        acc.statement()
        acc.deposit(100)
        print(f"Calculated Interest: ${acc.calculate_interest():.2f}")
        print("-" * 40)