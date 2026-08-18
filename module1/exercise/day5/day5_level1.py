# ==========================================
# Level 1: Basic Inheritance Exercises
# ==========================================

# 1. Simple Inheritance - Vehicle Class Hierarchy
class Vehicle:
    def __init__(self, name: str, model: str, year: int):
        self.name = name
        self.model = model
        self.year = year

    def info(self):
        """Prints general vehicle information."""
        print(f"Vehicle: {self.year} {self.name} {self.model}")


class Car(Vehicle):
    def __init__(self, name: str, model: str, year: int, num_doors: int):
        super().__init__(name, model, year)
        self.num_doors = num_doors  # Unique attribute

    def open_trunk(self):
        """Unique method for Car."""
        print(f"The trunk of the {self.name} is now open.")


class Motorcycle(Vehicle):
    def __init__(self, name: str, model: str, year: int, has_sidecar: bool):
        super().__init__(name, model, year)
        self.has_sidecar = has_sidecar  # Unique attribute

    def wheelie(self):
        """Unique method for Motorcycle."""
        print(f"The {self.name} is performing a wheelie!")


# Base Account class for Exercises 2 & 3
class Account:
    def __init__(self, owner: str, balance: float = 0.0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount: float):
        if amount > 0:
            self.balance += amount
            print(f"[{self.owner}] Deposited ${amount:.2f}. Balance: ${self.balance:.2f}")

    def withdraw(self, amount: float):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"[{self.owner}] Withdrew ${amount:.2f}. Balance: ${self.balance:.2f}")
        else:
            print(f"[{self.owner}] Insufficient funds.")


# 2. Savings Account Inheritance
class SavingsAccount(Account):
    def __init__(self, owner: str, balance: float = 0.0, interest_rate: float = 0.05):
        super().__init__(owner, balance)
        self.interest_rate = interest_rate  # Unique attribute (e.g., 5% = 0.05)

    def add_interest(self):
        """Calculates and deposits earned interest into balance."""
        interest = self.balance * self.interest_rate
        self.balance += interest
        print(f"[{self.owner}] Added interest of ${interest:.2f}. New Balance: ${self.balance:.2f}")


# 3. CurrentAccount Inheritance
class CurrentAccount(Account):
    def __init__(self, owner: str, balance: float = 0.0, overdraft_limit: float = 500.0):
        super().__init__(owner, balance)
        self.overdraft_limit = overdraft_limit  # Unique attribute

    def withdraw(self, amount: float):
        """Overrides withdraw() to allow overdraft up to specified limit."""
        if amount <= 0:
            print("Withdrawal amount must be positive.")
            return

        if self.balance - amount >= -self.overdraft_limit:
            self.balance -= amount
            print(f"[{self.owner}] Withdrew ${amount:.2f}. Current Balance: ${self.balance:.2f}")
        else:
            print(f"[{self.owner}] Transaction declined: Exceeds overdraft limit of ${self.overdraft_limit:.2f}")


# --- Testing Level 1 ---
if __name__ == "__main__":
    print("--- 1. Vehicle Hierarchy Test ---")
    car = Car("Toyota", "Corolla", 2022, 4)
    car.info()
    car.open_trunk()

    moto = Motorcycle("Yamaha", "MT-07", 2021, False)
    moto.info()
    moto.wheelie()

    print("\n--- 2. Savings Account Test ---")
    sav = SavingsAccount("Habtamu", 1000.0, 0.05)
    sav.add_interest()

    print("\n--- 3. Current Account Test ---")
    curr = CurrentAccount("Abebe", 200.0, 300.0)
    curr.withdraw(400.0)  # Utilizes overdraft
    curr.withdraw(200.0)  # Exceeds overdraft limit