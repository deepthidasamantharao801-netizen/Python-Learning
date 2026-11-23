
#a,b=map(int,input("Enter the values:").split())
#print(a,b)
try:
    a,b=map(int,input("Enter the values:").split())
    print(a,b)
    result=a/b
    print(f'Answer is {result}')
except  Exception as e:
    print(f'Error is {e}')

#Multiple Except Blocks
try:
    a,b=map(int,input("Enter the values:").split())
    #print(a,b)
    result=a/b
    print(f'Answer is {result}')
except ValueError:
    print("Values should be only 2 and only integers")
except ZeroDivisionError:
    print("Cannot divide by zero")
except NameError:
    print("Sarigga chusi rayu")


 
try:
    subjects=['Python',45,'AI',30]
    #print(subjects[5])
    subjects.append("SQL")
    print(subjects)
except Exception as e: #This can be written if you want exception to take care
    print(e)
except IndexError:
    print("Make sure to check the spelling")
except NameError:
    print("Check the spelling")
except AttributeError:
    print("Check the method properly")
finally:
    print("Anyways this will be printed.....")



#Cathing Multiple Exceptions Together
try:
    value=int(input("Enter a value:"))
    f=10/value
    print(f)
except(ValueError,ZeroDivisionError,NameError) as e:
    print(f'An Error occured:{e}')

#Raising Exceptions
#You can raise exceptions intentionally using raise keyword
value=15
if value<0:
    raise ValueError("Value cannot be negative")
else:
    print("Done")

Custom Error Messages:
try:
     raise Exception("Custom Error Message")
except Exception as e:
     print(e)


try:
     value=-15
     if value<0 or value in [1,20]:
        raise ValueError("Value is negative")
except Exception as e:
     print(e)




File Handling  ------>open()

File and Directory operations are essential to store data..
Python Provides  Built-In functions aclled ------> open()

#mode of operations ------> 'r','w','r+','w+'
#open(filena,.mode) #default mode is 'r'
try:  
     file=open('ABCD.txt',"r")
     print(file)
     #print(file.read()) 9#reads the entire content
     #print(file.readline()) #reads a single line
     print(file.readlines()) #read all lines into a list
except Exception as e:
     print(e)



     
