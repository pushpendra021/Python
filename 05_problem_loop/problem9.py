items = ["apple", "banana", "orange", "apple", "mango"]

for i in range(len(items)):  
    for j in range(i + 1, len(items)):  
        if items[i] == items[j]:  # Compare elements
            print("Duplicate found:", items[i])
            exit()  # Exit immediately if duplicate found

print("All elements are unique")
