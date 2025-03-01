# its print even number but type is list
def even_generator(num):
    list=[]
    for i in range(2,num+1,2):
        list.append(i)

    return list
result=even_generator(10)
print(result)
print(type(result))

#generate a even number
def generate(limit):
    for i in range(2,limit+1,2):
        yield i

for i in generate(10):
    print(i)
