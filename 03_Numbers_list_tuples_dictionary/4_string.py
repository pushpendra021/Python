chai_type="Masala"
quantity=5
order="I ordered {} cups of {} chai"
print(chai_type)
print(quantity)
print(order)
print("-----placeholder methods for formating------")
print(order.format(quantity,chai_type))


print("list to string")
l1=['Lemon','Ginger','masala','chai']
print(" ".join(l1))
print(", ".join(l1))

print("-----lenth method-----")
print(len(order))


print("---how to use for loop in string----")
for char in chai_type:
    print(char)

str1="This ensures that \"extra spaces\" are removed in sentence"
print(str1)
str2="Masala\nChai"
print(str2)

str3=r"Masala\nChai"
print(str3)


str4=r"c:\\user\\pwd\\"
print(str4)

str5=r"c:\user\pwd"
print(str5)


str6="masala chai"
print("masala" in str6)
print("masalaa" in str6)