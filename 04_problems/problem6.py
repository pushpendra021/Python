distance=int(input("Enter distance"))
if distance<0:
    print("Please enter vailid distance")
    exit()
if distance<3:
    print("walk")
elif distance<=15:
    print("Bike")
elif distance>15:
    print("Car")