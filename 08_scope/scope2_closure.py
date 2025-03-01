x=99
def fun3():
    #x=88
    def fun2():
        print(x)
    return fun2
myresult=fun3()
print(myresult)
myresult()