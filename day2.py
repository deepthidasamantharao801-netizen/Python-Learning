'''
datatypes-->it will tell us how to define the data
'''
#python by default follows implicit type
#numeric datatypes --> integer --> quantities,ids,order ids,stock,age -->int
'''age = 22
print(age)
print(type(age))
stock = 35
print(type(stock))
batch_rank = 1
print(batch_rank)
'''
#float values -->salaries,price,percentage calculations,temp.... -->float
'''
salary = 15125.45
print(salary)
print(type(salary))
'''
#complex --> real and imaginary values
'''
data = 3+5j
print(data)
print(type(data))
'''
#boolean --->true/false --->validations
'''access = True
print(type(access))
result = False
print(type(result))
'''
#nonetype -->none
#none -->0,false,'',[],(),{},set()-->none cases in python
'''branch_rank = None
print(type(branch_rank))
'''
#typecoversion-->converting one datatype to another datatype
'''
rank=5
print(type(rank))
b=float(rank)
print(b)
print(type(b))
c = complex(rank)
print(c)
d = bool(rank)
print(d)
print(type(d))
'''
'''
int()
0
bool()
False
float()
0.0
complex()
0j
bool(0)
False
bool(None)
False
bool('')
False
bool([])
False
bool([''])
True
bool([0])
True
bool(' ')
'''
'''price = 43.25
b = int(price)
print(b)
print(type(b))
c = complex(price)
print(c)
print(type(c))
d = bool(price)
print(d)
print(type(d))
'''
#complex -->int,float,bool
'''signal = 5+6j
a = bool(signal)
print(a)
b = int(signal)#raises typeError
print(b)
c = float(signal)
print(c)
'''

'''access = True
a = complex(access)
print(a)
b = int(access)
print(b)
c = float(access)
print(c)
'''
'''a = int(float(bool(5)))
print(a)
'''
'''a = bool(float(int(35)))
print(a)
c = True+35+3.5+(6+5j)
print(c)
'''
'''#sequence types --> strings,lists,sets,frozensets,dictionaries
#strings-->group of characters
#quotations-->single,double,triple quotes
place = 'codegnan'
print(type(place))
name = 'deepthi'
print(name)
#strings are immutable,orderded,indexed collection
print(len(name))#len(obj)-->returns the number of items in a collection
print(len(place))
print(len('qwerty'))
print(len('dasamantharao deepthi'))
a = ' '
print(a)
print(len(a))
'''
#converting string -->int,float,complex,boolean
course = 'python'
#print(int(course))
#print(float(course))
#print(complex(course))
print(bool(course))


data = 56
b = str(data)
print(b)
mileage = 13.5
c = str(mileage)
print(type(c))
d = str(3+5j)
print(d)
e = str(true)
print(e)
