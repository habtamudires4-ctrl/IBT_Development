# Level 2: Intermediate Exercises
# 4. Student Class
class Student:
    def __init__(self, name, student_id):
        # Initializes student info with an empty list for grades.
        self.name = name
        self.student_id = student_id
        self.grades = []

    def add_grade(self, grade: float):
        # Adds a grade to the student's list of grades.
        if 0 <= grade <= 100:
            self.grades.append(grade)
            print(f"Grade {grade} added for {self.name}.")
        else:
            print("Invalid grade! Must be between 0 and 100.")

    def average_grade(self) -> float:
        # Calculates and returns the average grade.
        if not self.grades:
            return 0.0
        return sum(self.grades) / len(self.grades)


# 5. Product Class
class Product:
    def __init__(self, name, price, stock):
        # Initializes product name, price, and stock level.
        self.name = name
        self.price = price
        self.stock = stock

    def sell(self, quantity: int):
        # Reduces stock when selling, preventing negative inventory.
        if quantity <= 0:
            print("Quantity to sell must be greater than zero.")
        elif quantity <= self.stock:
            self.stock -= quantity
            print(f"Sold {quantity} unit(s) of {self.name}. Stock left: {self.stock}")
        else:
            print(f"Cannot sell {quantity} items. Only {self.stock} available in stock.")

    def restock(self, quantity: int):
        # Increases stock count.
        if quantity > 0:
            self.stock += quantity
            print(f"Restocked {quantity} unit(s) of {self.name}. Total stock: {self.stock}")
        else:
            print("Restock quantity must be positive.")


# 6. Encapsulation Practice (Account with Private Balance)
class EncapsulatedAccount:
    def __init__(self, owner: str, balance: float = 0.0):
        self.owner = owner
        self.__balance = balance  # Private attribute balance

    @property
    def balance(self) -> float:
        # Read-only property/getter for balance.
        return self.__balance

    def withdraw(self, amount: float):
        # Withdrawal method with strict validation.
        if amount <= 0:
            print("Withdrawal amount must be greater than zero.")
        elif amount > self.__balance:
            print(f"Transaction declined, Insufficient funds. Balance: ${self.__balance:.2f}")
        else:
            self.__balance -= amount
            print(f"Successfully withdrew ${amount}. Balance remaining: ${self.__balance:.2f}")


# --- Testing Level 2 by creating objects
if __name__ == "__main__":
    print("--- 4. Testing Student Class ---")
    student = Student("Habtamu", "SQ10/IBT000265")
    student.add_grade(88.5)
    student.add_grade(92.0)
    student.add_grade(95.5)
    print(f"Average Grade for {student.name}: {student.average_grade()}")

    print("\n--- 5. Testing Product Class ---")
    laptop = Product("Dell XPS 15", 1500.0, 10)
    laptop.sell(3)
    laptop.sell(10)  # Attempt to sell more than stock
    laptop.restock(5)

    print("\n--- 6. Testing Encapsulated Account Class ---")
    enc_acc = EncapsulatedAccount("Habtamu", 1000.0)
    print(f"Account Balance (via Property): ${enc_acc.balance}")
    enc_acc.withdraw(200)
    # enc_acc.__balance  # Un-commenting this line would throw an AttributeError