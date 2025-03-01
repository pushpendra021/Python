dic1={"Masala":"Spicy","Ginger":"Zesty","Green":"Mild"}
print("-------Dictionary------")
print(dic1)
print(type(dic1))
print(dic1["Masala"])
print(dic1.get("Ginger"))
print(dic1.get("Lemon"))
# print(dic1["Lemon"])  error

dic1["Green"]="Fresh"
print(dic1)

print("print all keys")
for tea in dic1:
    print(tea, end=" ")


print('')
print("print all values")
for tea in dic1:
    print(dic1[tea], end=" ")


print('')
print("print in key pairs")
for tea in dic1:
    print(tea, dic1[tea])

print("----new way to apply for loop-------")
for key,value in dic1.items():
    print(key,value)


if "Masala" in dic1:
    print("I have Masala tea")
    print(dic1["Masala"])

print(len(dic1))

dic1["Lemon"]="Citrus"
print(dic1)

print("------pop method---------")
print(dic1.pop("Ginger"))
print(dic1)

print(dic1.popitem())
print(dic1)

del dic1["Green"]  # Correct way
print(dic1)


print("-----Count keys and Values------")
count = list(dic1.values()).count("Spicy")
print(count)
count = list(dic1.keys()).count("Masala")
print(count)

print("-------copy dictionary with difference memory----")
dic2=dic1.copy()
print(dic2)

