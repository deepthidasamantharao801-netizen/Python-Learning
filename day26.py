
reduce() --->it reduces an iterable into a single value .. it
repeatedly applies a function to combine elements..
we can use it from functools

import functools
from functools import reduce
#sum of numbers from a iterable
numbers = [1,5,2,3,4]
result = reduce(lambda a,b:a+b,numbers)
print(result)

#larger number from a collection

import functools
from functools import reduce
data = list(map(int,input().split()))
print(data)
result = reduce(lambda a,b: a if a>b else b,data)
print(result)

#Return the longest word in a group of strings

words = ['Python','Developer','SQL','Programming']
longest = reduce(lambda a,b : a if len(a) > len(b) else b, words)
print(f'Longest Word : {longest}')

#list comprehension -->In python ,it is a precise way to create
#Lists
#Syntax --->[expression for item in iterable]
#iterable --->list,set,dict,or range()

li =[]
for i in range(10):
    print(i)
    li.append(i)
print(li)

li = [i for i in range(10)]
print(li)

#square of 1-10 numbers in a list
squares = [i**2 for i in range(1,11)]
print(squares)

#even number 1-10 numbers in a list
even = [i%2==0 for i in range(1,11)]
print(even)
even_numbers = [i for i in range(1,11) if i%2==0]
print(even_numbers)

#update scores of each person  with 10 marks
scores =[25,45,27,20,59]
f_scores =[i+10 for i in scores]
print(f_scores)

m_scores = list(map(lambda i:i+10,scores))
print(m_scores)

names = ['gowthu','codegnan','vizag']
#result = ['GOWTHU',CODEGNAN','VIZAG']
result = [i.upper() for i in names]
print(result)
 # for using map 
result = list(map(lambda i:i.upper(),names))
print(result)

#list comprehension with if-else usage
#[true_value if condition else false_value for item in iterable ]
data=[12,4,5,6,8,9]
result =["Even" if i%2==0 else "odd" for i in data]
print(result)

result =[i**2 if i%2==0 else i**3 for i in data]
print(result)

#nested list comprehensions --->one inside another
#[expression for i in iterable1 for j in iterable2]
colours =['Red','Blue','White']
sizes = ['S','M','L','XL']
dress = [(colour,sizes) for colour in colours for size in sizes]
print(dress)

d= [(i,j) for i in range(1,5) for j in range(1,5)]
print(d)
print(*d)
