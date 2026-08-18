# Level 3: Advanced Exercises

# 7. Full Bank Account with Properties
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = max(0.0, balance)

    @property
    def balance(self) -> float:
        # Getter for balance.
        return self.__balance

    @balance.setter
    def balance(self, value: float):
        # Setter for balance with input validation.
        if value < 0:
            print("Error: Balance cannot be negative.")
        else:
            self.__balance = value

    def deposit(self, amount: float):
        # Deposits money if amount is positive.
        if amount > 0:
            self.__balance += amount
            print(f"[{self.owner}] Deposited ${amount}. Balance: ${self.__balance:.2f}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount: float) -> bool:
        # Withdraws money if sufficient funds exist.
        if amount <= 0:
            print("Amount must be positive.")
            return False
        if amount <= self.__balance:
            self.__balance -= amount
            print(f"[{self.owner}] Withdrew ${amount}. Balance: ${self.__balance:.2f}")
            return True
        print(f"[{self.owner}] Transaction failed: Insufficient funds.")
        return False

    def transfer(self, to_account: "BankAccount", amount: float):
        # Transfers money to another BankAccount instance.
        if self.withdraw(amount):
            to_account.deposit(amount)
            print(f"Transferred ${amount} from {self.owner} to {to_account.owner}.")


# 8. Library System
class Book:
    def __init__(self, title: str, author: str, isbn: str):
        self.title = title
        self.author = author
        self.isbn = isbn
        self._available = True  # Encapsulated state

    @property
    def available(self) -> bool:
        return self._available

    def borrow(self) -> bool:
        if self._available:
            self._available = False
            return True
        return False 
    def return_item(self):
        self._available = True


class Library:
    def __init__(self):
        self.__books = []  # Private list of Book objects

    def add_book(self, book: Book):
        """Adds a book object to the library collection."""
        self.__books.append(book)
        print(f"Added '{book.title}' to the library.")

    def borrow_book(self, isbn: str):
        """Finds a book by ISBN and borrows it."""
        for book in self.__books:
            if book.isbn == isbn:
                if book.borrow():
                    print(f"Successfully borrowed '{book.title}'.")
                else:
                    print(f"Sorry, '{book.title}' is currently checked out.")
                return
        print("Book with this ISBN not found.")

    def return_book(self, isbn: str):
        """Finds a book by ISBN and returns it."""
        for book in self.__books:
            if book.isbn == isbn:
                book.return_item()
                print(f"Successfully returned '{book.title}'.")
                return
        print("Book with this ISBN not found.")


# 9. Car Class with Encapsulation
class Car:
    def __init__(self, make: str, model: str):
        self.make = make
        self.model = model
        self.__speed = 0.0  # Private speed
        self.__fuel = 100.0  # Private fuel level (percentage)

    @property
    def speed(self) -> float:
        return self.__speed

    @property
    def fuel(self) -> float:
        return self.__fuel

    def accelerate(self, increment: float):
        """Increases speed if fuel is available."""
        if self.__fuel <= 0:
            print("Out of fuel! Cannot accelerate.")
            return
        self.__speed += increment
        self.__fuel = max(0.0, self.__fuel - (increment * 0.1))
        print(f"Accelerated to {self.__speed} km/h. Fuel left: {self.__fuel:.1f}%")

    def brake(self, decrement: float):
        """Reduces speed down to a minimum of 0."""
        self.__speed = max(0.0, self.__speed - decrement)
        print(f"Braked. Current speed: {self.__speed} km/h")

    def refuel(self, amount: float):
        """Refuels car up to 100% capacity."""
        if amount > 0:
            self.__fuel = min(100.0, self.__fuel + amount)
            print(f"Refueled. Current fuel: {self.__fuel}%")


# --- Testing Level 3 ---
if __name__ == "__main__":
    print("--- 7. Testing Bank Account & Transfer ---")
    acc1 = BankAccount("Habtamu", 1000.0)
    acc2 = BankAccount("Abebe", 300.0)
    acc1.transfer(acc2, 400.0)

    print("\n--- 8. Testing Library System ---")
    lib = Library()
    b1 = Book("Clean Code", "Robert C. Martin", "978-0132350884")
    lib.add_book(b1)
    lib.borrow_book("978-0132350884")
    lib.borrow_book("978-0132350884")  # Attempt borrowing again
    lib.return_book("978-0132350884")

    print("\n--- 9. Testing Car Class ---")
    car = Car("Toyota", "Corolla")
    car.accelerate(50)
    car.brake(20)
    car.refuel(10)