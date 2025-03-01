number=int(input("Enter a number"))
sum=0
for val in range(0,number+1):
    if val%2==0:
        sum+=val
print("Sum of positive number : ",sum)