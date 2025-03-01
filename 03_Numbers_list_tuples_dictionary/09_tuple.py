#tuple ()--->inmmutable
t1=("Black","Green","Oolong")
print(t1)
print(t1[2])
print(t1[-2])
print(t1[:])
print(t1[1:])
print(t1[-3:])


# error 
# t1[1]="Lemon"
# print(t1)

# we can change reference but not value
print(len(t1))

t2=("Herbal","Earl Grey")
t3=t1+t2
print(t3)
if "Herbal" in t3:
    print("I have Herbal tea")

counting=t3.count("Herbal")
print(counting)

(Lemon,Wine,Cofee)=t1
print(Lemon)
print(type(t1))

#nested tuple--->("",(),"")
t4=("Apple","Banana",("Orange","Graph"),("Pineapple",("tea","Chai")))
print(t4)
print(t4[0])
print(t4[2])
print(t4[2][1])
print(t4[3])
print(t4[3][0])
print(t4[3][1][1])