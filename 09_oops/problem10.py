# First parent class
class Battery:
    def __init__(self, battery_size):
        self.battery_size = battery_size

    def battery_info(self):
        return f"Battery Size: {self.battery_size} kWh"

# Second parent class
class Engine:
    def __init__(self, horsepower):
        self.horsepower = horsepower

    def engine_info(self):
        return f"Engine Power: {self.horsepower} HP"

# Child class inheriting from both Battery and Engine
class ElectricCar(Battery, Engine):
    def __init__(self, brand, model, battery_size, horsepower):
        Battery.__init__(self, battery_size)  # Initialize Battery class
        Engine.__init__(self, horsepower)     # Initialize Engine class
        self.brand = brand
        self.model = model

    def display_info(self):
        return f"{self.brand} {self.model}"

# Creating an instance of ElectricCar
my_tesla = ElectricCar("Tesla", "Model S", 100, 670)

# Displaying information
print(my_tesla.display_info())   # Tesla Model S
print(my_tesla.battery_info())   # Battery Size: 100 kWh
print(my_tesla.engine_info())    # Engine Power: 670 HP

# Checking multiple inheritance
print(isinstance(my_tesla, ElectricCar))  # True
print(isinstance(my_tesla, Battery))      # True
print(isinstance(my_tesla, Engine))       # True
print(isinstance(my_tesla, object))       # True
