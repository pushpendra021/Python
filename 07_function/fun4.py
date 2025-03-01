def area(radius):
    Area=3.1417*(radius**2)
    Circum_ference=2*3.1417*radius
    return Area,Circum_ference

radius=int(input("Enter a radius : "))
tuple=area(radius)
print(tuple)

a,c=area(radius)
print("----------A and C----",a," ",c)