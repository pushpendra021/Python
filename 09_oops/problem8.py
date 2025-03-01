class Car:
    def __init__(self, brand, model):
        self.__brand = brand
        self.__model = model  # Private attribute

    def Display_info(self):
        return f"{self.__brand} {self.__model}"
    
    # Static method
    @staticmethod
    def general_description():
        return "Cars are means of transport"
    
    # Property (getter)
    @property
    def model(self):
        return self.__model


# Create an object
my_car1 = Car("Tata", "Mahendra")

# Access model as an attribute, NOT as a method
print(my_car1.model)   # ✅ Correct
# print(my_car1.model()) ❌ Incorrect (Raises TypeError)
