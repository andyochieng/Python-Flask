class Employee:
    def __init__(self, name, salary):
        self.__name = name
        self.salary = salary
        self.dateofreg = "10-31-2024"

    def display_employee(self):
        return f"Employee Name: {self.name}, Salary: {self.salary}: {self.dateofreg}"

    def update_salary(self, amount):
        if amount > 0:
            self.salary += amount
        else:
            print("Salary can't be negative")
emp1 = Employee("Andy", 5000)
print(emp1.display_employee())
print(emp1.__name)
print(emp1.update_salary(100))
print(emp1.display_employee())