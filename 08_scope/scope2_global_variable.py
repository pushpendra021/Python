x=100
def fun():
    print(x)
fun()

def fun1():
    global x
    x=120
    print(x)
fun1()