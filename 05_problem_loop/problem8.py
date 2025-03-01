number=int(input("Enter number"))
flag=True
if number<=0:
    print("Number is invalid")
    exit()

for i in range(2,number):
    if number%i==0:
        print("Number is not prime")
        flag=False
        break

if flag==True:
    print("Given number is prime")
