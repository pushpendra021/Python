coffee = input("Enter coffee size: ").lower()
option= input("Enter option: ").lower()

if coffee=="small" and option !="extra shot":
    print(f"confirm a {coffee} coffee.")
elif coffee in ["medium","large"] or (coffee == "small" and option =="extra shot"):
    print(f"confirm a {coffee} coffee with an extra shot.")
else:
    print("Enter valid coffee size")