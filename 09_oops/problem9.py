# Base class
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def display_info(self):
        return f"{self.brand} {self.model}"

# Derived class (inherits from Car)
class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)  # Call parent constructor
        self.battery_size = battery_size

    def battery_info(self):
        return f"Battery Size: {self.battery_size} kWh"

# Creating an instance of ElectricCar
my_tesla = ElectricCar("Tesla", "Model S", 100)

# Displaying information
print(my_tesla.display_info())  # Tesla Model S
print(my_tesla.battery_info())  # Battery Size: 100 kWh

# Using isinstance() function
print(isinstance(my_tesla, ElectricCar))  # True
print(isinstance(my_tesla, Car))          # True

#isinstance(my_tesla, object) → ✅ True (Every class in Python inherits from object)

print(isinstance(my_tesla, object))       # True
print(isinstance(my_tesla, str))          # False
