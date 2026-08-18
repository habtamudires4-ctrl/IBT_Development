from abc import ABC, abstractmethod


# ==========================================
# 1. Single Responsibility Principle (SRP)
# ==========================================

class Employee:
    def __init__(self, name: str, salary: float):
        self.name = name
        self.salary = salary


class SalaryCalculator:
    def calculate_bonus(self, employee: Employee) -> float:
        return employee.salary * 0.10


class EmployeeRepository:
    def save_to_file(self, employee: Employee, filename: str):
        with open(filename, "a") as f:
            f.write(f"{employee.name},{employee.salary}\n")


class EmailService:
    def send_email(self, employee: Employee, message: str):
        print(f"Sending email to {employee.name}: {message}")


# ==========================================
# 2. Open/Closed Principle (OCP)
# ==========================================

class EmployeeRole(ABC):
    @abstractmethod
    def calculate_bonus(self, salary: float) -> float:
        pass


class Manager(EmployeeRole):
    def calculate_bonus(self, salary: float) -> float:
        return salary * 0.20


class Developer(EmployeeRole):
    def calculate_bonus(self, salary: float) -> float:
        return salary * 0.15


class Intern(EmployeeRole):
    def calculate_bonus(self, salary: float) -> float:
        return salary * 0.05


def calculate_employee_bonus(role: EmployeeRole, salary: float) -> float:
    return role.calculate_bonus(salary)


# ==========================================
# 3. Liskov Substitution Principle (LSP)
# ==========================================

class Bird:
    def __init__(self, name: str):
        self.name = name

    def move(self):
        print(f"{self.name} is moving.")


class FlyingBird(Bird):
    def fly(self):
        print(f"{self.name} is flying high!")


class Eagle(FlyingBird):
    pass


class Penguin(Bird):
    def swim(self):
        print(f"{self.name} is swimming in cold water.")


def make_bird_fly(bird: FlyingBird):
    bird.fly()


# ==========================================
# Execution & Demonstration
# ==========================================
if __name__ == "__main__":
    emp = Employee("Habtamu", 5000.0)
    calc = SalaryCalculator()
    repo = EmployeeRepository()
    email = EmailService()

    print(f"Bonus: ${calc.calculate_bonus(emp)}")
    email.send_email(emp, "Welcome aboard!")

    dev_role = Developer()
    print(f"Developer Bonus: ${calculate_employee_bonus(dev_role, 5000.0)}")

    eagle = Eagle("Ethiopian Eagle")
    make_bird_fly(eagle)