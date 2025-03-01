class Car:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model
    
    def Display(self):
        return f"{self.brand} {self.model}"
        
#child class
class Electric_car(Car):#iski wajaha se car ki sabhi properties aa gayi hai
    def __init__(self,brand,model,battery_size):
        super().__init__(brand,model)
        self.battery_size=battery_size


my_electric_car=Electric_car("Tesla","Model S","85kwh")
print(my_electric_car.brand)
print(my_electric_car.model)
print(my_electric_car.battery_size)

print("Access child class")
print(my_electric_car.Display)
print(my_electric_car.Display())