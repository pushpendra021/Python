str = input("Enter Your Password: ")
n=len(str)
if n==0:
    print("Enter atleast 1 lenth password")
    exit()
if n<6:
    print("Weak passwor.")
elif n<=10:
    print("Medium passwor")
else:
    print("Strong passord")