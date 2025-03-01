year=int(input("Enter any year: "))

if year%400==0:
        print("Leap year")
elif (year%100!=0 and year%4==0):
        print("Leap year")  
else:
    print("Not a leap year")