str1="   masala chai   "
print(str1)
print("strip method-------------",str1.strip())
print("replace method",str1.replace("masala","ginger"))
print("using two method",(str1.replace("masala","ginger")).strip())

print("replace method",str1.replace("masala chai","ginger"))
print("replace method",str1.replace("Lemon","ginger"))


print("---------string to list-------------------")
str2="Lemon, Ginger, Masala, Mint"
print("Bydefault include space : ",str2.split())
print("split using , (comma and space): ",str2.split(", "))

print("--------find method---------")
print(str1.find("chai"))
print("if not find then return -1 by default" ,str1.find("Chai"))


str3="masala chai chai chai chai"
print(str3.find("chai"))
print("---------count method--------")
print(str3.count("chai"))
