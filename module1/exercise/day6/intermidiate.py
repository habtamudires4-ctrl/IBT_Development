from abc import ABC, abstractmethod


# ==========================================
# 1. Apply SRP + DIP
# ==========================================

class INotifier(ABC):
    @abstractmethod
    def send(self, message: str):
        pass


class IRepository(ABC):
    @abstractmethod
    def save(self, data: str):
        pass


class EmailNotifier(INotifier):
    def send(self, message: str):
        print(f"[Email] {message}")


class DatabaseRepository(IRepository):
    def save(self, data: str):
        print(f"[Database] Saved: {data}")


class Account:
    def __init__(self, owner: str, balance: float, notifier: INotifier, repo: IRepository):
        self.owner = owner
        self.balance = balance
        self.notifier = notifier  # Dependency Injection
        self.repo = repo          # Dependency Injection

    def withdraw(self, amount: float):
        if amount <= self.balance:
            self.balance -= amount
            self.notifier.send(f"Withdrew ${amount}. Balance: ${self.balance}")
            self.repo.save(f"Withdrawal of ${amount} for {self.owner}")


# ==========================================
# 2. Factory Pattern
# ==========================================

class BaseAccount(ABC):
    def __init__(self, owner: str, number: str, balance: float):
        self.owner = owner
        self.number = number
        self.balance = balance


class SavingsAccount(BaseAccount):
    pass


class CurrentAccount(BaseAccount):
    pass


class FixedDepositAccount(BaseAccount):
    pass


class AccountFactory:
    @staticmethod
    def create(kind: str, owner: str, number: str, balance: float) -> BaseAccount:
        kind = kind.lower()
        if kind == "savings":
            return SavingsAccount(owner, number, balance)
        elif kind == "current":
            return CurrentAccount(owner, number, balance)
        elif kind == "fixed":
            return FixedDepositAccount(owner, number, balance)
        else:
            raise ValueError(f"Unknown account type: {kind}")


# ==========================================
# 3. Observer Pattern
# ==========================================

class Observer(ABC):
    @abstractmethod
    def update(self, account_number: str, amount: float):
        pass


class SMSAlert(Observer):
    def update(self, account_number: str, amount: float):
        print(f"[SMS ALERT] Large withdrawal detected! Acc: {account_number}, Amount: ${amount:.2f}")


class AuditLog(Observer):
    def update(self, account_number: str, amount: float):
        print(f"[AUDIT LOG] Security record logged for Acc: {account_number}, Amount: ${amount:.2f}")


class ObservableAccount(BaseAccount):
    def __init__(self, owner: str, number: str, balance: float):
        super().__init__(owner, number, balance)
        self._observers: list[Observer] = []

    def attach(self, observer: Observer):
        self._observers.append(observer)

    def withdraw(self, amount: float):
        if amount <= self.balance:
            self.balance -= amount
            if amount > 3000:
                self._notify(amount)

    def _notify(self, amount: float):
        for observer in self._observers:
            observer.update(self.number, amount)

# ==========================================
# 4. Interface Segregation Principle (ISP)
# ==========================================

class IInterestBearing(ABC):
    @abstractmethod
    def calculate_interest(self) -> float:
        pass


class ISPSavingsAccount(BaseAccount, IInterestBearing):
    def calculate_interest(self) -> float:
        return self.balance * 0.05


class ISPCurrentAccount(BaseAccount):
    # Current accounts are not forced to implement interest methods
    pass