class Car:
    total_car=0

    def __init__(self,brand,model):
        self.brand=brand
        self.model=model
        Car.total_car+=1
    def Display_info(self):
        return f"{self.brand} {self.model}"
    
    #how to create a static method
    # in static method me self nahi likhna hota hai
    @staticmethod
    def general_description():
        return "Cars are means of transport"


my_car1=Car("Tata","Mahendra")
print(my_car1.Display_info())

# print(my_car1.general_description())
print(Car.general_description())


