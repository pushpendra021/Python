species = input("Enter pet species (Dog/Cat): ").strip().lower()
age = int(input("Enter pet age in years: "))

if species == "dog":
    if age < 2:
        print("Recommendation: Puppy food")
    else:
        print("Recommendation: Adult dog food")

elif species == "cat":
    if age > 5:
        print("Recommendation: Senior cat food")
    else:
        print("Recommendation: Regular cat food")

else:
    print("Invalid species! Please enter 'Dog' or 'Cat'.")
