# actual how to work *args
def sum_element(*args):
    print(args)
    print(type(args))
    print(*args)
    sum1=0

    #can apply loop-->yes
    for i in args:
        print(i*2)
        sum1+=i
    

    print(sum1)# using loop
    return sum(args)#use args concept

print(sum_element(1,2,3))





#solution fun7
def sum_element(*args):
    return sum(args)

print(sum_element(1,2,3))
