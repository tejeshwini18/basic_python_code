class Employee:
    company = "TCS"   # Class variable (shared by all objects)

    def __init__(self, name, salary):
        self.name = name      # Instance variable
        self.salary = salary  # Instance variable


emp1 = Employee("Alice", 50000)
emp2 = Employee("Bob", 60000)

print(emp1.company)  # TCS
print(emp2.company)  # TCS

emp1.salary = 55000
print(emp1.salary)  # 55000
print(emp2.salary)  # 60000 (unchanged)
