
functions --> a reusable block of code which performs a specific task

def fname(parameters):#Function header
     """doc string(description of function)"""
     statement(s).....#body of function
     .........
     return value(s)
     fname(args)#actual arguments

there are 5 arguments
   1. postional arguments --->count of arguments to be matched
   2.default arguments ----> we can make argumrnts as default
   3.keyword arguments---->order/keyword name to be matched
   4.variable length arguments --->we can pass any number of postional arguments
   5.keyword variable length arguments(**kwargs)  -->we can pass any number of keyword arguments


#positional arguments -->count of arguments to be matched
def data(a,b,c):
    """function to perform arithmetic operations"""
    d = a+b+c
    e = a-b-c
    f = a*b*c
    g = a/b/c
    return d,e,f,g
print(data(12,3,1))


d,e,f = map(int,input().split())
result = data(d,e,f)
print(f'Result is {result}')


#default arguments -->we can give arguments as default
def data(a,b=5,c=2):#non-default arguments always follows default arguments
    """function to perform arithmetic operations"""
    d = a+b+c
    e = a-b-c
    f = a*b*c
    g = a/b/c
    return d,e,f,g
print(data(2,3,4))
print(data(12))
print(data(12,3))
print(data())#mandatory count to be matched
print(data(a=34))
#print(data(a=34,3,5)) position arguments follows keyword arguments



#keyword arguments -->keyword name to be matched
#grocery purchace
def grocery(item,price=40):
    """usage of keyword arguments"""
    print(f'Item is {item}')
    print(f'value of item is {price}')
grocery('cova bun')#it takes default
grocery('milk',30)
grocery(30,'curd')
print(grocery(price = 30,item = 'curd'))#returns none also output
#grocery(items='cova',price=100) #type error keyword argument mismatch

#variable length arguments -->we can capture any number of positional arguments
#we use (*args),captures excess positional arguments and pack them into tuple..
def sample(*a):
    """usage of arbitrary arguments"""
    print(a)
    print(type(a))
sample()
sample(1,2,)
sample([12,3,4,5,6])
sample('deepu','codegnan')
































     
