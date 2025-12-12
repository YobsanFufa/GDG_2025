class Employee:
    def __init__(self, name,salary):
        self.name = name 
        self.salary =salary
    def annual_salary(self):
        return 12*self.salary
s1 = Employee("Beka", 56000)
print(f"{s1.name}'s annual salary is {s1.annual_salary()}")
