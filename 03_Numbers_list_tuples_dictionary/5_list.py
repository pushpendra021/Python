l1=['Black','Green','Oolong','White']

print(l1)
print("----------Slicing method on list----------")
print(l1[1])
print(l1[-1])
print(l1[0:3])
print(l1[-4:])
print(l1[2:])
print(l1[0:4:2])

print("---------update-------")
l1[2]='Masala chai'
print(l1)

print("------Insert method-------")
l1.append("Masala")
print(l1)
l1.insert(1,'Ginger')
print(l1)

print("------pop method------")
l1.pop()
print(l1)
l1.remove('Masala chai')
print(l1)

l1[1:2]="Lemon"
print(l1)

l1[1:2]=["Lemon"]
print(l1)

l1[1:3]=['chai','tea']
print(l1)

print("---index method----")
print(l1.index("Green"))

