class Car:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model
    
    def Display(self):
        return f"{self.brand} {self.model}"
        


my_car=Car("Tata","Mahindra")
print(my_car.brand)
print(my_car.model)
print(my_car.Display())