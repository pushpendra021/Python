age=int(input("Enter your age : "))
day=input("Enter day name: ")

if age<18 and day!="Wednesday":
    print("Ticked price is : $8")
elif age>=18 and day!="Wednesday":
    print("Ticked price is : $12")
elif day=="Wednesday":
    if age<18:
        print("Every one get discount : $",8-2)
    else:
        print("Every one get discount : $",12-2)
