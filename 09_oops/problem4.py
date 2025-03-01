class Car:
    def __init__(self,model):
        self.model=model
        self.__brand = None  # Private attribute
    
    def setter(self,brand):
        self.__brand=brand

    def getter(self):
        return self.__brand
    
my_car=Car("Safari")
my_car.setter("TATA")
print(my_car.getter())
print(my_car.model)
