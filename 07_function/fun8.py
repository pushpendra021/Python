def print_kwargs(name,power):
    print("name ",name,"Power :",power)

# both function output is same because of name arguments
print_kwargs(name="Pushpendra",power="lazer")
print_kwargs(power="lazer",name="Pushpendra")


# kwargs arguments
print("--- kwargs arguments---")
def kwargs(**kwargs):
    for key,value in kwargs.items():
        print(f"{key}: {value}")

kwargs(name="Pushpendra",power="lazer")
kwargs(power="lazer",name="Pushpendra")
kwargs(name="Pushpendra")
kwargs(power="lazer")