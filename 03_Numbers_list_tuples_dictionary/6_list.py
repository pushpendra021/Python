l1=['Black','Green','Oolong','White']
print(l1[1:1])

l1[1:1]=["tea","tea"]
print(l1)

print(l1[1:3])
l1[1:3]=[]
print(l1)

for str in l1:
    print(str,end=' ')


print(" ")
for str in l1:
    if str=='Green':
        continue
    print(str)

if 'Green' in l1:
    print("I have Green tea")

l2=l1  # inside memory have same memory references
l3=l1.copy() # inside memory have difference refernce

l4=l2+l3
print(l4)

print(range(10))
squared_numbers=[x**2 for x in range(0,10)]
print(squared_numbers)