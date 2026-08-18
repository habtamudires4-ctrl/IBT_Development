# ==========================================
# Level 3: Advanced Account Hierarchy
# ==========================================
from abc import ABC, abstractmethod

class Account(ABC):
    def __init__(self, owner: str, balance: float = 0.0):
        self.owner = owner
        self._balance = max(0.0, balance)  # Protected attribute

    @property
    def balance(self) -> float:
        """Read-only property for account balance."""
        return self._balance

    def deposit(self, amount: float):
        if amount > 0:
            self._balance += amount
            print(f"[{self.owner}] Deposited ${amount:.2f}. Balance: ${self._balance:.2f}")
        else:
            print("Deposit amount must be positive.")

    @abstractmethod
    def withdraw(self, amount: float) -> bool:
        pass

    @abstractmethod
    def statement(self):
        pass

    @abstractmethod
    def calculate_interest(self) -> float:
        pass


class SavingsAccount(Account):
    def __init__(self, owner: str, balance: float = 0.0, interest_rate: float = 0.05):
        super().__init__(owner, balance)
        self._interest_rate = interest_rate

    @property
    def interest_rate(self) -> float:
        return self._interest_rate

    def withdraw(self, amount: float) -> bool:
        if 0 < amount <= self._balance:
            self._balance -= amount
            print(f"[{self.owner}] Withdrew ${amount:.2f}. Balance: ${self._balance:.2f}")
            return True
        print(f"[{self.owner}] Insufficient funds for withdrawal.")
        return False

    def calculate_interest(self) -> float:
        return self._balance * self._interest_rate

    def add_interest(self):
        interest = self.calculate_interest()
        self._balance += interest
        print(f"[{self.owner}] Applied interest: ${interest:.2f}. New Balance: ${self._balance:.2f}")

    def statement(self):
        print(f"[Savings Account] Owner: {self.owner} | Balance: ${self._balance:.2f} | Interest: {self._interest_rate * 100}%")


class CurrentAccount(Account):
    def __init__(self, owner: str, balance: float = 0.0, overdraft_limit: float = 500.0):
        super().__init__(owner, balance)
        self._overdraft_limit = overdraft_limit

    @property
    def overdraft_limit(self) -> float:
        return self._overdraft_limit

    def withdraw(self, amount: float) -> bool:
        if amount > 0 and (self._balance - amount >= -self._overdraft_limit):
            self._balance -= amount
            print(f"[{self.owner}] Withdrew ${amount:.2f}. Balance: ${self._balance:.2f}")
            return True
        print(f"[{self.owner}] Transaction rejected: Overdraft limit exceeded.")
        return False

    def calculate_interest(self) -> float:
        return 0.0

    def statement(self):
        print(f"[Current Account] Owner: {self.owner} | Balance: ${self._balance:.2f} | Overdraft Limit: ${self._overdraft_limit:.2f}")


# Bonus Challenge: FixedDepositAccount inheriting from SavingsAccount
class FixedDepositAccount(SavingsAccount):
    def __init__(self, owner: str, balance: float, lock_period_months: int, interest_rate: float = 0.10):
        super().__init__(owner, balance, interest_rate)
        self.lock_period_months = lock_period_months
        self.is_locked = True

    def withdraw(self, amount: float) -> bool:
        if self.is_locked:
            print(f"[{self.owner}] Withdrawal failed: Funds are locked for {self.lock_period_months} months.")
            return False
        return super().withdraw(amount)

    def unlock_account(self):
        """Unlocks account after term completion."""
        self.is_locked = False
        print(f"[{self.owner}] Fixed Deposit account has unlocked.")

    def statement(self):
        status = "Locked" if self.is_locked else "Unlocked"
        print(f"[Fixed Deposit] Owner: {self.owner} | Balance: ${self._balance:.2f} | Lock: {self.lock_period_months} mo ({status})")


# --- Testing Level 3 ---
if __name__ == "__main__":
    print("--- 7 & Bonus Test ---")
    fd = FixedDepositAccount("Habtamu", 10000.0, lock_period_months=12)
    fd.statement()
    fd.withdraw(1000.0)  # Fails due to lock
    fd.unlock_account()
    fd.withdraw(1000.0)  # Succeeds