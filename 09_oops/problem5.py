class Car:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model
    def Display_info(self):
        return f"{self.brand} {self.model} {self.fuel_type}"
    
    def fuel_type(self):
        return "Diesel or Petrol"
    
class Electric_car(Car):
    def __init__(self,brand,model,battery_size):
        super().__init__(brand,model)
        self.battery_size=battery_size
     


    def Display_info(self):
        return f"{self.brand} {self.model} {self.battery_size} {self.fuel_type}"
    
    def fuel_type(self):
        return "Electric Charge"
    
my_electric=Electric_car("Tesla","Model S","85kwh")
print(my_electric.fuel_type())


my_car=Car("Tata","Mahendra")
print(my_car.fuel_type())
