str=input("Enter your string : ")
char_count={} # used to store counting same as map -->dictionary

for char in str:
    char_count[char]=char_count.get(char,0)+1 #in initialy used 0 at position 

unique_char="#"
for char in str:
    if char_count[char]==1:
        unique_char=char
        break
if unique_char=="#":
    print("Unique character is not present")
else:
    print(unique_char)