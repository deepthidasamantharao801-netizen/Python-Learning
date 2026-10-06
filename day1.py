'''
name = "deepthi"
age = 22
place = "vizag"
email_id = "deepthi@codegnan.com"#snakecase convention(multiple words)
print(email_id)
branch_1 = "vizag"#we can use number anywhere but not at the start 
print(branch_1)
#true = 45 #as true is a keyword we cannot use as variable
'''
'''
#comments-->it will make users understand what it is conveying
#single line comment-->#
#multi line comments-->we can use triple quotes(doc string)
name,email_id,mobile,gender = "deepthi","deepthi@codegnan.com",8341653599,"female"
name = "nikki";age=20;place="vizag" 
print(name,age)
'''
'''
#deletion-->del
del age
del name,place #permanant deletion
print(age)
'''
''''
#swapping of variables
a,b=15,25
print(a)
print(b)
a,b=b,a#value of a will become b
print(a)
print(b)
c=a#reassigning the existing value to a new variable
print(c)
'''
'''
#literals--> these are constants such as numbers(int,float,complex)
#"hello" "good"
age=32
print(age)
taste = "bad"
print(taste)
price=115.45
print(price)
print(type(price))#it returns the type of object
#type()is very very imp
print(type(age))
'''

#identifiers-->names given to variables,functions,classes,objects,modules

#punctuators-->[]-->lists,{}-->dictonaries,sets,()-->tuples
a=5
b=3
print(a/b)
print(a//b)
print(a%b)
