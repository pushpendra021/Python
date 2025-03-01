str1='abc xyz'
str2="def"
str3="""Ghi"""
print(str1)
print(str2)
print(str3)

print("first characte",str1[1])
print("Last character",str1[-1])
print("slicing : ",str1[0:3])
print("slicing : ",str1[-3:-1])
print("slicing : ",str1[-3:])


l1="0987654321"
print(l1)
print(l1[:])
print(l1[3:])
print(l1[:7])
print("skip one number from starting: ",l1[0:7:2])#2-->skip one number
print("skip two number from starting: ",l1[0:7:3])#3-->skip two number

print("Negative numbers")
print(l1[-3:])
print(l1[:-7])
print("skip one number : ",l1[-1:-7:-2])#2-->skip one number
print("skip two number : ",l1[-1:-7:-3])#3-->skip two number

print(str1.upper())
print(str3.lower())

print("COncatination")
print(f"{str1}{str3}")
print(str1+str3)
print(f"{str1} {str3}")
print(" ".join([str1, str3]))
print(str1+" " +str3)