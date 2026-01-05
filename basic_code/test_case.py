# Write a class Employee with attributes name, salary, and a method display()

class Employee:
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary

    def display(self):
        return self.name,self.salary
    
e = Employee("Tejeshwini",20000)
n,s=e.display()
print(n,s)

