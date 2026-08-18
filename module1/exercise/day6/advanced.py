from abc import ABC, abstractmethod


# Singleton Bank Configuration
class BankConfig:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.savings_interest_rate = 0.07
            cls._instance.overdraft_limit = 1000.0
            cls._instance.large_transaction_threshold = 3000.0
        return cls._instance


# Observer Interface
class Observer(ABC):
    @abstractmethod
    def update(self, acc_num: str, amount: float):
        pass


class SMSAlert(Observer):
    def update(self, acc_num: str, amount: float):
        print(f"[SMS] Large transaction alert for account {acc_num}: ${amount:.2f}")


# Base Abstract Account
class Account(ABC):
    def __init__(self, owner: str, number: str, balance: float):
        self.owner = owner
        self.number = number
        self._balance = balance
        self._observers: list[Observer] = []

    def attach(self, observer: Observer):
        self._observers.append(observer)

    def _notify_large_transaction(self, amount: float):
        config = BankConfig()
        if amount >= config.large_transaction_threshold:
            for obs in self._observers:
                obs.update(self.number, amount)

    @abstractmethod
    def withdraw(self, amount: float) -> bool:
        pass


# Concrete Account Implementations
class SavingsAccount(Account):
    def withdraw(self, amount: float) -> bool:
        if amount <= self._balance:
            self._balance -= amount
            self._notify_large_transaction(amount)
            return True
        return False


class InvestmentAccount(Account):  # Refactoring Challenge - New Account Type
    def __init__(self, owner: str, number: str, balance: float):
        super().__init__(owner, number, balance)
        self.investment_return_rate = 0.12

    def withdraw(self, amount: float) -> bool:
        if amount <= self._balance:
            self._balance -= amount
            self._notify_large_transaction(amount)
            return True
        return False


# Account Factory supporting seamless addition of InvestmentAccount
class AccountFactory:
    @staticmethod
    def create(kind: str, owner: str, number: str, balance: float) -> Account:
        kind = kind.lower()
        if kind == "savings":
            return SavingsAccount(owner, number, balance)
        elif kind == "investment":
            return InvestmentAccount(owner, number, balance)
        else:
            raise ValueError(f"Invalid account type: {kind}")