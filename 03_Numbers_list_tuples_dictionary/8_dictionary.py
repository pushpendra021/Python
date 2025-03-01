
print('kya dictionary ke inside another dictionary bana sakte hai')

#{{},{}}
tea_shop={
    "chai":{"Masala":"Spicy","Ginger":"Zesty"},
    "Tea":{"Green":"Mild","Black":"Strong"},
    "Lemon":"Citurs"
}

print("-----------How to access----- ")
print(tea_shop)
print(tea_shop["chai"])
print(tea_shop["chai"]["Masala"])
print(tea_shop["Tea"]["Black"])
print(tea_shop["Lemon"])

#in list
squared_number_list=[x**2 for x in range(6)]
print(squared_number_list)

#il dictionary
squared_number_dic={x:x**2 for x in range(6)}
print(squared_number_dic)
squared_number_dic.clear()
print(squared_number_dic)

print("--------How to create new dictionary using list and some default value")
list1=["Masala","Ginger","Lemon"]
default_value="Delicious"

new_dic=dict.fromkeys(list1,default_value)
print(new_dic)


new_dic1=dict.fromkeys(list1,list1)
print(new_dic1)

