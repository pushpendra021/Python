#1,2,3---->decimal number 
#4+5j---->complex
# 0o--->Octal Number
# 0x--->hexa decimal
# 0b1000-->Binary Number
# oct(64)-->octal conversion
# hex(64)-->hexadecimal
# bin(64)---->binary conversion
#int(3.14)-->integer
# int('64',8)--->string to octal(base 8 conversion)
# int ('64',16)-->string to hexadecimal (base 16 conversion)
# int('1000',2)-->string to binary
import random
l1=[1,2,3,4,5,6]
print(random.random())
print(random.random())
print(random.randint(1,10))
print(random.randint(1,10))
print(random.choice(l1))
print(random.choice(l1))
random.shuffle(l1)
print(l1)
random.shuffle(l1)
print(l1)


setone={1,2,3,4}
#intersection of set
print("intersection of set : ",setone & {1,4})
print("Union of set : ",setone | {1,4,8,9})
print("difference of set : ",setone - {1,4,8,9})




