'''
Built-in Functions --> Functions which are inbuiltin Python
abs(),any(),all(),bin(),bool()......
dir(__builtins__)-->enumerate(),zip()

details = ['codegnan','deepthi','pfs-vsp-007']

0:codegnan
1:deepthi
2:pfs-vsp-007

for i in details:
    print(details.index(i),':',i)
for i in range(len(details)):
    print(i,':',details[i])

for i,j in enumerate(details):
    print(f'{i}:{j}')


#enumerate() will create a counter object for an iterable
#zip() will combine multiple iterables into a single iterable

data = ['deepthi','mamatha','gowthami']
marks = (20,22,25)
#place = ('vizag','vjwda','hyd')
details = dict(zip(data,marks))#if we take one more iterable it raises ValueError
print(details)



emails = input().split()
print(emails)
for email in emails:
    print(email.split('@')[1])


orders = list(map(int,input().split()))
print(orders)


#eval()--> you can take any input-->dict
salaries = eval(input("Enter the Salaries:"))
print(salaries)
print(type(salaries))


print(int(4.56))
print(round(4.67)) #round() it will round off to next decimals/nearest value 
print(round(4.678,2))


#Function is termed as First class object
#Recursive Functions --->A function calling itself,where it makes the smaller problem is broken into multiple times...
#depends on two cases -->Base case(it indicates when to stop recursion)
                    #--> Recursive case(it makes the problem to be repeated)
#suitable for tree structures,graph traversal....

Syntax:
def function():
    if base_condition:
        return
    function() #we write our recursive
function()

#Factorial Approach using Recursion

def factorial(n):
    """Recursive Approach"""
    if n==0 or n==1:
        return 1
    elif n<0:
        return "No -ve values only +ve values to be accepted"
    else:
        return n*factorial(n-1)
n = int(input('Enter a Value:'))
print(factorial(n))

#Sum of Natural numbers using recursive logic
#5 -->15 #1+2+3+4+5

def add(n):
    """Recursive Approach"""
    if n==0 or n==1:
        return 1
    elif n<0:
        return "No -ve values only +ve values to be accepted"
    else:
        return n+add(n-1)
n = int(input('Enter a Value:'))
print(add(n))

Task: Built a Simple Choice Chooser:
1 -->Recursion logic Factorial
2-->sum of natural numbers(recursion)
3-->BMI calculation
4-->Fibonacci series
5-->ATM Usecase
any other number -->only enter 1-5
Q-->Quit
'''


def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)


def sum_natural(n):
    if n == 0:
        return 0
    return n + sum_natural(n - 1)


def bmi_calculation():
    weight = float(input("Enter weight in kg: "))
    height = float(input("Enter height in meters: "))

    bmi = weight / (height * height)
    print("Your BMI is:", round(bmi, 2))


def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


def atm():
    balance = 10000

    while True:
        print("\n1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            print("Available Balance:", balance)

        elif choice == "2":
            amount = float(input("Enter deposit amount: "))
            balance += amount
            print("Amount deposited successfully.")

        elif choice == "3":
            amount = float(input("Enter withdrawal amount: "))

            if amount <= balance:
                balance -= amount
                print("Please collect your cash.")
            else:
                print("Insufficient balance.")

        elif choice == "4":
            print("Thank you for using ATM.")
            break

        else:
            print("Invalid choice.")


while True:
    print("\n========== SIMPLE CHOICE CHOOSER ==========")
    print("1. Factorial using Recursion")
    print("2. Sum of Natural Numbers using Recursion")
    print("3. BMI Calculation")
    print("4. Fibonacci Series")
    print("5. ATM Usecase")
    print("Q. Quit")

    choice = input("\nEnter your choice: ").upper()

    if choice == "1":
        n = int(input("Enter a number: "))
        if n < 0:
            print("Factorial is not defined for negative numbers.")
        else:
            print("Factorial:", factorial(n))

    elif choice == "2":
        n = int(input("Enter a number: "))
        if n < 0:
            print("Enter a positive number.")
        else:
            print("Sum:", sum_natural(n))

    elif choice == "3":
        bmi_calculation()

    elif choice == "4":
        n = int(input("Enter number of terms: "))
        if n <= 0:
            print("Enter a positive number.")
        else:
            print("Fibonacci Series:")
            for i in range(n):
                print(fibonacci(i), end=" ")
            print()

    elif choice == "5":
        atm()

    elif choice == "Q":
        print("Thank you! Program terminated.")
        break

    else:
        print("Please enter only 1-5 or Q.")



























































