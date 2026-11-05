# Inheritance
class Employee:
    def __init__(self,name, email, department, salary):
        self.name = name
        self.email = email
        self.department = department
        self.salary = salary
    def show_details(self):
        print(self.name, self.department, self.salary)

class PermanentEmployee(Employee): #inheriting
    def __init__(self, name, email, department, salary, cover, increment):
        super().__init__(name, email, department, salary) # makes sure the parents class sets up the values in it
        self.cover = cover # set up extra params that we need for the class
        self.increment = increment

class ContractEmployee(Employee):
    def __init__(self, name, email, department, salary, tenure):
        super().__init__(name, email, department, salary)
        self.tenure = tenure

p1 = PermanentEmployee("Jane Mark", "jm@yahoo.com", "HR", 100_000, "Britam", 4)
c1 = ContractEmployee("jin Jung", "jj@gmail.com", "sales", 88_000, 3)

p1.show_details()
c1.show_details()

# TODO overriding
# oop in python tutorial
# classes in python tutorial

