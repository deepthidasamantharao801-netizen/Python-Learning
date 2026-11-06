
while --> initialized statement,counter....

#banking scenario-->pin authentication if more than 3 attempts account locked

pin = '3145'
max_attempts = 3
current_attempt = 0
while current_attempt < max_attempts:
    enter_pin = input('enter the atm pin')
    if enter_pin == pin:
        print('login successful')
        print('withdraw the money')
        break
    else:
        print('entered pin is wrong.try again carefully')
        current_attempt += 1
else:
    print('account locked....try again after 24hours')


#BMI Scenario (usecase),we will make use of control block statements:

#BMI -->body mass index-->bmi = weight(kgs) / (height**2) (meters)

feet ---> 1 feet --->12 inches -->2.54cm --->30.48cms
     ---->5 feet 6 inches --->167.78cms ---> 1.67 meters

weight = int(input('enter the weight in kgs:'))
height = float(input('enter the height in meters:'))
bmi = (weight)/((height)**2)
print(bmi)

#print(bmi)
#(<18.5 -->underweight,18.5 - 24.9 -->healthy,25 - 29.9--->overweight ,>=30 --->obesity)

n = int(input('how many users:'))
for i in range(n):
        weight = int(input('enter the weight in kgs:'))
        height = float(input('enter the height in meters:'))
        name = input('enter the name:')
        if weight>0 and height>0:
            bmi = (weight)/((height)**2)
            if bmi<18.5:
                print(f'{name} --->you are underweight as bmi is {bmi}')
            elif bmi>=18.5 and bmi<=24.9:
                print(f'{name} --->you are in perfect physique,bmi is {bmi}')
            elif bmi>=25 and bmi<=29.9:
                print(f'{name} --->you are overweight need to maintain diet,bmi is {bmi}')
            elif bmi>=30:
                print(f'{name} --->obesity,bmi is {bmi}')
        else :
            print(f'enter only +ve values')


#task :--->for same above bmi calculator,store the details in dictionaries

#bmi_results = {'names':[user1,user2,user3....],
#                       'bmi_values':[bmi1,bmi2....]

#o/p format:
#bmi_results = {'names':['deepu','nikki','vicky'],
#                       'bmi_values':[24.657,25.456,28.945]



#assert ---> It is mainly used in debugging checking during development
#it tests whether given condition is satisfied or not its
#a mandatory else it will raise the error.It is mainly used
# to catch bugs
#by ensuring the conditions hold True..


x = int(input('enter the value:'))
#assert x>0
assert x>0,"enter only positive value"
x = x**2
print(f'final result is {x}')
assert x in [24,25,12,10],"checking data"
print(f'search found')






#task :--->for same above bmi calculator,store the details in dictionaries

#bmi_results = {'names':[user1,user2,user3....],
#                       'bmi_values':[bmi1,bmi2....]

#o/p format:
#bmi_results = {'names':['deepu','nikki','vicky'],
#                       'bmi_values':[24.657,25.456,28.945]





bmi_results = {
    'names': [],
    'bmi_values': []
}

n = int(input("Enter number of users: "))

for i in range(n):
    name = input("Enter your name: ")
    weight = float(input("Enter your weight in kg: "))
    height = float(input("Enter your height in meters: "))

    bmi = weight / (height ** 2)

    bmi_results['names'].append(name)
    bmi_results['bmi_values'].append(round(bmi, 3))

print("\nBMI Results:")
print(bmi_results)


























        
        
