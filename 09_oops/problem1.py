# create a class
class Car:
    #__init__() ---->is a constructor
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model

#create a object
my_car=Car("Toyota","Corolla")

#how to acces class value
print(type(my_car))
print(my_car.brand)
print(my_car.model)

