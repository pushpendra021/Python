while True:
    number=int(input("Enter a number between 1 and 10: "))
    if number>=1 and number<=10:
        print("Valid input! you entered ",number)
        break
    else:
         print("Invalid input. Try again.")
