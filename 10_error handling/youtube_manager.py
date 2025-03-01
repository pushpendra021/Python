f=open("text.txt",mode='w')
if f:
    print("Succesfylly file open")
else:
    print("File not found")

#proper code for file handling
try:
    f.write("Chai aur code")
finally:
    f.close()

#update syntax
with open('text.txt',mode='w') as file:
    file.write("Code with python")