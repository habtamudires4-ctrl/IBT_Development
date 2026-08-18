print("My name is Habtamu this is my first python class exercise")
# 1. Simple Class - Person
class Person:
    def __init__(self, name, age):
        # Constructor to initialize name and age attributes.
        self.name = name
        self.age = age

    def introduce(self):
        # Prints a personalized greeting message.
        print(f"Hello! My name is {self.name} and I am {self.age} years old.")

# 2. Rectangle Class
class Rectangle:
    def __init__(self, length: float, width: float):
        """Constructor to initialize dimensions."""
        self.length = length
        self.width = width

    def area(self) -> float:
        """Calculates and returns the area of the rectangle."""
        return self.length * self.width

    def perimeter(self) -> float:
        """Calculates and returns the perimeter of the rectangle."""
        return 2 * (self.length + self.width)


# 3. Bank Account (Basic)
class Account:
    def __init__(self, owner: str, balance: float = 0.0):
        """Constructor to initialize account owner and initial balance."""
        self.owner = owner
        self.balance = balance

    def deposit(self, amount: float):
        """Deposits specified amount into account balance."""
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount}. New balance: ${self.balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount: float):
        """Withdraws specified amount if funds are available."""
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew ${amount}. Remaining balance: ${self.balance}")
        else:
            print("Insufficient funds!")



if __name__ == "__main__":
    print("--- 1. Testing Person Class ---")
    p1 = Person("Habtamu", 26)
    p2 = Person("Abebe", 30)
    p1.introduce()
    p2.introduce()

    print("\n--- 2. Testing Rectangle Class ---")
    r1 = Rectangle(10, 5)
    r2 = Rectangle(7, 3)
    print(f"R1 -> Area: {r1.area()}, Perimeter: {r1.perimeter()}")
    print(f"R2 -> Area: {r2.area()}, Perimeter: {r2.perimeter()}")

    print("\n--- 3. Testing Basic Account Class ---")
    acc = Account("Habtamu", 500.0)
    acc.deposit(200.0)
    acc.withdraw(150.0)
    acc.withdraw(1000.0) 