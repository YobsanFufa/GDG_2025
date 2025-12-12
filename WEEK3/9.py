class Vehicle:
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year
    def info(self):
        return f"Vehicle Brand: {self.brand}, Year: {self.year}"
class Car(Vehicle):
    def __init__(self, brand, year, model):
        super().__init__(brand, year)  # Call parent constructor
        self.model = model
    def info(self):
        return f"Car Brand: {self.brand}, Year: {self.year}, Model: {self.model}"
v1 = Vehicle("BMW", 2003)
c1 = Car("BMW", 2003, "X5")
print(v1.info())  
print(c1.info()) 
