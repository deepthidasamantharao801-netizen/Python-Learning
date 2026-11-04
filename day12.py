'''#if statement programs
===========================
product_sales = int(input())
if product_sales > 1000:
    print("Best Seller")
else:
    print("No Output")
============================
#Zepto
delivery_charges = bool(input())
print(type(delivery_charges))
print(delivery_charges)
if delivery_charges:
    print("Extra Rain Charges Applied")
else:
    print("No Output") #we will get this when we dont pass any input
============================
#Delivery Charge Calculation
order_value = int(input())
if order_value > 99:
    print(f"Final Bill Amount:{order_value}")
else:
    print(f"Final Bill Amount:{order_value + 30}")

=============================
budget = int(input("Enter the value"))
if budget>10000:
    print("Plan:Trip")
elif budget>5000:
    print("Plan:Resort Stay")
elif budget>3000:
    print("Plan:Movie and Dinner")
elif budget>1000:
    print("Plan:Cafe and Shopping")
elif budget>500:
    print("Plan:Street Food and Park Visit")
else:
    print("plan:Stay Home")
==============================
'''
#Repetation Statements (Loops) --> Loops helps us in automating repetative
#tasks -->for,while
#Usage of for: --> It is used mainly to iterate within in lists,strings,ranges
'''
Syntax:
for <temp> in collection/range:
statements(s)....
...........
..........

marks = [25,22,27,28,29,30]
marks = list(map(int,input("Enter the marks:").split(",")))
for i in marks:
    print(i) #it traverses within the loop


marks = list(map(int,input("Enter the marks:").split(",")))
total = 0
for mark in marks:
    #print(i) #it traverses within the loop
    #we need to update total with each mark
    total = mark + total #total += mark
    print(total)
print(f"Total marks are:{total}")
print(f"Avg marks are:{total/len(marks)}")
==================================
subject = input("Enter the Subject:")
for i in subject:
    print(i)
'''
details = {'ids':[121,122,123],
           'marks':[20,22,30]}
for data in details: #indexed through keys
    print(data)
    print(details[data]) #it returns values

for data in details.values():
    print(data)
for k,v in details.items():
    print(k,v)




