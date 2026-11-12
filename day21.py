
def sample(*a):
    """usage of arbitrary arguments"""
    print(a)
    print(type(a))
sample()
sample(1,2,)
sample([12,3,4,5,6])
sample('deepu','codegnan')


#in above case we used '*' to pack the values into a tuple
a,b,c = 2,4,-6
print(a,b,c)
a,*b,c = 2,4,5,6,64,31,-12
print(a)
print(c)
print(b) # in this case all values are stored into list

#a,*b,*c = 2,4,5,6,64,31,-12 #multiple expressions are not allowed..
#print(a)
#print(c)
#print(b) 

#a,*b,c = (2,4,5),(6,64),31,-12
#print(a)
#print(c)
#print(b)


def add(*a):
    "usage of variable length aruguments"""
    #print(a)
    #print(type(a))
    result = 0
    print(a)
    for value in a:
        #if type(value) in (int,float) -->membership operator
        if type(value)== int or type(value)== float: #comparision and logical operators
            result = result+value
            #print(result)
    return result
#print(add())
#print(add(1,2,3,4,5,6,7))#sum of this is 28
#print(add(98,78,65,-400))#sum of this is -159
#print(add(1,2,3,-2,'codegnan',2,11,'deepu'))
d = list(map(int,input().split()))
print(d)
print(add(*d)) # we need to use * to unpack the values from the tuple


#we will use above usage of variable length arguments for ordering pizza
def order_pizza(size,*toppings):
    """usage of *args"""
    print(f'Size of Pizza is {size}')
    #print(f'Toppings:{toppings}')
    for topping in toppings:
        print(f'Topping added :{topping}')
order_pizza('large','onions','paneer','capsicum','olives','mushroom')


#keyword variable length arguments:any number of keyword arguments,data is stored in dictionary,we use **kwargs..

def sample(**a):
    """usage of **kwargs"""
    print(a)
    print(type(a))
sample()
sample(name='deepu',batch='pfs-vsp-007',place='vizag',branch='ece',course='pfs') 




def order_pizza(size,*toppings,**details):
    """usage of *args"""
    print(f'Size of Pizza is {size}')
    #print(f'Toppings:{toppings}')
    for topping in toppings:
        print(f'Topping added :{topping}')
    for key,value in details.items():
        print(f'Data is {key},result is {value}')
order_pizza('large','onions','paneer','capsicum','olives','mushroom',name='deepu',bill=200,delivery=False,tip=50)





















































