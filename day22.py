'''
#usage of variable length and keyword variable length arguments

def scores(*marks,branch = 'codegnan',**names):
    """scores scenario with variable and keyword variable length args"""
    print(marks)
    print(names)
    total = 0
    for mark in marks:
        if type(mark) in (int,float):
            total += mark
    print(f'Total marks are:{total}')
    for name,value in names.items():
    #for name in names.values():
        print(f'Name:{name}')
        print(f'Value:{value}')
        print(f'Branch is {branch}')
scores(25,20,19,18,21,name='Deepu',place='vizag',batch='PFS-VSP-007')
#positional arguments always follows keyword arguments
#non default always follows default args
'''

#Scope --> determines where a variable can be accessed within a program
#A variable is only accessible within the region where it is defined...
'''
Types of scope:local scope,global scope,global keyword,nonlocal scope


#Local Scope:Variables defined/declared and accessible only inside the function...

def fname():
    """usage of local variables"""
    name = 'codegnan'
    return f'{name} is in vizag'
print(fname())
#print(name)#NameError as LocalScope name inside the function
print(fname())
name = 'Deepu'
print(name)


#Global variable/scope-->A variable declared outside all functionsis called a global variable
#it can be accessed from anywhere in the program 
name = 'Codegnan'
def uname():
    """global scope"""
    return f'{name} is in Vizag,Vijayawada and Hyderabad.'
print(uname())
print(name)


#Local variables get higher priority inside the function
name = 'Codegnan'
def uname():
    """global scope"""
    name = 'Deepthi'
    return f'{name} is in Vizag,Vijayawada and Hyderabad.'
print(uname())
print(name)



#Global Keyword-->used when we want to modify a global variable inside the function

count = 15
def update():
    """Global Keyword usage"""
    global count
    count = count+5#UnboundLocalError so we need to use global keyword
    return f'Updated count is {count}'
print(update())
print(f'New Count is {count}')
values = [1,2,3]
values.append(count)
print(values)

#NonLocal Scope--> used in nested functions..allows modifications of variables from the outer function

def outer():
    """Outer Function"""
    count = 10
    def inner():
        """Inner Function"""
        nonlocal count
        count = count+15
        return f'Result from Inner function is {count}'
    print(inner())
    return f'Result from Outer function is {count}'
print(outer())

#LEGB -->Local,Enclosing-->Global--->Built-in

len = 32
a =['codegnan','python']
#print(len(a)) #Here we have used built-in function as identifier it fails



#Functions are termed as first class objects
#pass by value and pass by object reference

#pass by value -->Immutable objects
#int,float,bool,str,tuple,complex,frozenset
#when immutable objects are passed to function,changes inside the function
#donot effect the original value

def update(number):
    """Pass by value usage"""
    number = 15
    print("Inside Function:",number)
number = 20    
update(number)
print("Outside value is",number)

'''

def update(number):
    """Pass by value usage"""
    return number*3
   #print("Inside Function:",number)
number = 20    
print(update(number))
print(update(25))















































