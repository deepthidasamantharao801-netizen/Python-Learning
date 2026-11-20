
data=[i*j for i in range(1,11) for j in range(1,11)]
#print(data)
for table in data:
    print(table,end=" ")

#Nested Comprehension with if condition
#Syntax:[expression for i in iterable1 for j in iterable2 if condition]
data=[(i,j) for i in range(1,4) for j in range(1,4) if i!=j]
print(data)

f=[i*j for i in range(1,4) for j in  range(1,4) if i!=j]
print(f)
print(*f)

#nested Comprehension with if-else usage
#[true_value if condition else false_value for item1 in iterable
#for item2 in iterable2]

week_1=[15,20,25,22,18,19]
week_2=[23,19,21,18,19,25]

result=["Improved" if x>y else "Lagged" for x in week_1 for y in week_2]
print(result)
#make sure to check the braces and closures
#In the above case if we replace [] braces with() ---->we dont get tuple

#Generators
#result=("Improves" if x>y else "Lagged" for x in week_1 for y in week_2)
#print(result)

#Generator  ---> It is a Special Function, which produces one value at a time
#we use yield keyword
def func():
    '''Normal Function'''
    return[1,2,3,4,5]
    #return "Saketh" # A function can have return with multiple values
#print(func())
data = func()
for i in data:
    print(i)


def func():
    '''Generator Function'''
    yield 1
    yield 2
    yield 3
#print(func())
b = func()
print(next(b))
print(next(b))
print(next(b))
print(next(b))
#print(next(b)) It raises StopIteration as values are already fetched

def display():
    '''Subjects Covered'''
    yield ["Python",45,'Paperbased Exams']
    yield ["Aptitude",65,'Weekly Exams']
    yield ["Softskills",60,'Activities']
    yield ["Frontend",45,'Projects']
    yield ["FASTAPI",45,'Integration']
print(display())
g=display()
print(f'Subject alloted is {next(g)}')
print(f'Subject alloted is {next(g)}')
print(f'Subject alloted is {next(g)}')

week_1=[20,14]
week_2=[15,20]
result=("Improved" if x<y else "Lagged" for x in week_1 for y in week_2)
#print(result)
g=result
print(next(g))
print(next(g))
print(*(result))




#Exception Handling
#Exception is an  event that occurs during the execution of a program
#which disrupts its normal flow...

#TypeError,ValueError,IndexError,AttributeError,KeyError,ZeroDivisionError.

#We will be using try,except and finally...

"""
Syntax:
try:
      #code that raise an exception
except ExceptionType:
      #code to handle the exception
"""

#Basic Exception handling
a,b=5,0
try:
    result=a/b
    print(f'Answer is {result}')
except Exception as e:
    print(f'Error is {e}')



