
#Pass by Reference -->When mutable objects(Lists,Sets,dict) are passed into the function,changes inside the function effect the original object...

def update(items):
    """we will assume items as list"""
    #items.append('laptop')
    items.extend(['laptop','power bank','camera'])
cart = ['mobile','watch']
print(update(cart))#returns none
print(cart)#original list changes
#print(update('Deepthi'))#raises Attribute Error

#Dictionary Usage: -->Updating profile
def update(profile):
    """Usage of Dictionary"""
    profile['branch'] = "Vizag"
students = {'names':['Deepthi','Nikitha']}
pfs_students= {'batches':['pfs-vsp-007','pfs-vsp-006'],
            'subjects':['python','mysql']}
update(students)
print(students)
update(pfs_students)
print(pfs_students)
                                     

#pass by value-->original data will not change,immutable objects
#pass by object reference-->original will change,mutable objects


#Built-in Functions -->Functions which are inbuilt in python
#print(),len(),min(),max(),sorted(),int(),float(),bool(),complex(),str(),list(),set(),dict(),tuple(),input(),eval(),help()

#print(dir())
#print(dir(__builtins__))#return list of builtin functions and errors
#print(help(print))
#print(help(len))

#abs(),chr(),ord()
print(abs(-35))#returns the absolute value of a numbers
print(chr(67))
print(ord('@'))#returns the ASCII value
data = [23,25,56,0]
print(any(data))#any() -->compares bool(x) for any valuer -->True
print(all(data))#all()-->needs all values to be present
#print(all(None))
print(all([None]))
print(bin(6))#returns binary object



print(help(enumerate))
data = ['Deepthi','Nikitha','gowthami']
c = dict(enumerate(data))#by default it creates a counter object
print(c)

d = dict(enumerate(data,1))
print(d)




#Zip-->it combines multiple collections into a single collection
data = ['Deepthi','Nikitha','Vivek','Nikhil','Anil']
marks = [25,20,23,26,24]
f = dict(zip(data,marks))#zip checks for length matching
print(f)












































































