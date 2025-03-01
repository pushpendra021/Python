score=int(input("Enter your marks: "))
if score>100:
    print("please check your score again")
    exit()
if score<60:
    print("Grade: F")
elif score<=69:
    print("Grade: D")
elif score<=79:
    print("Grade: C")
elif score<=89:
    print("Grade: B")
else:
    print("Grade: A")