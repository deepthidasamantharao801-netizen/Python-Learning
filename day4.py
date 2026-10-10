'''
operators --> operators help us to perform operations between operands

Arthimatic operators -->+,-,*,/,**,//(integer or floor division)'%(modulus -->remainder)

assignment operators -->it helps to assign,update(increment),decrement

# = (assigning),+= (additon&assign),-=(sutraction&assign)
'''
'''data=20
print(data)
print(type(data))

stock=data
print(stock)

# increment the value of stock
stock=stock+5
print(stock)
print(data)

# decrement the value of stock
data=data-2
print(data)
stock-=data
print(stock)

data -= 2
print(data)

data *=2
print(data)
'''
'''stock=100
stock**=2
print(stock)
'''
'''#comparision operators(relational operators)-->it performs comparision
#between the operands and results in boolean true/false--->conditions
# ==, !=, <,<=,>,>=

name='vinay'
vinay_attendance=75
print(vinay_attendance==80)
print(vinay_attendance>=80)
print(vinay_attendance<=80)
print(vinay_attendance>80)
print(vinay_attendance<80)
print(vinay_attendance!=80)
'''
'''# logical operators -->and,or,not(keywords)
#and -->itneeds all conditions to be satisfied(two or more)
#or-->it needs any one condition to be satisfied
#not-->opp to existing

max_marks=80
vinay_marks=75
max_att=75
vinay_att=70

vinay_marks += 10
certificate = vinay_marks>=max_marks and vinay_att>=max_att
print(certificate)
chance = vinay_marks>=max_marks or vinay_att>=max_att
print(chance)

data = []
print(data)
print(not(data))#returns true
data = [1,2,3,4]
print(not(data))#returns false as data existing

#both logical and comparision operators will result in boolean
'''

'''#membership operators -->in,not in

names = ['deepu','nikki','vicky','anil']
name = 'bunny'
print(name in names)#returns false
print(name not in names)#returns true
print('12' in '121')
#print(12 in 121)#typeerror as we have taken int type
'''
'''print('ajay'in 'ajay kumar')#returns true as we are checking type as string
print(['ajay'] in ['ajay'])
'''

'''#identity operators-->it specifically refers to the object
#id-->is,is not
a=15
b=15
print(a==b)
print(id(a))
print(id(b))
c=a
print(id(c))
'''
'''a=(1,2,3)
b=(1,2,3)
print(a==b)
print(id(a))
print(id(b))
#as we have taken two lists eventhough with  similar values identity
print(a is b)
c=a
print(id(c))
print(c is a)#returns true as we are assigning to the same object

#when we check with the interpreter mode and scripting mode above
#tuple result changes
'''
'''#logical,membership,identity,comparision(relational) --->always result is in boolean
'''

#bitwise operators --> it performs bitwise operations -->&(bitwise and)
#| (bitwise or),^(bitwise xor)
#an integer will be converted binary format and performs bitwise operation
#following integer to binary conversions

print(7&3)
print(7|3)
print(7^3)

#shifting operators(<<,>>)
print(7<<1)#0111
print(7>>1)#0011
