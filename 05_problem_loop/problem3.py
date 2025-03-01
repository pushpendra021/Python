number=int(input("Enter number which you want to multiply: "))
for i in range(1,11):
    if i==5:
        continue
    print(f"{i} * {number} =",i*number)
