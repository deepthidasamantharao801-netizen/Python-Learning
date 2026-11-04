'''
Usage of for with conditional statements
normal completion -->loop is going through the entire sequence naturally.
interruption -->jumping statements(break,continue)

#notifications =[0,0,0,0]
notifications =[0,0,1,1,1,0,0]

#0 --> notification read
#1 --> unread notification
#notification checker
for notification in notifications:
    #you need to map a condition
    if notification ==1:
        print("unread notification")
else:
    print("all notifications are caught up")
#print("all notifications are caught up")
========================
#break -->terminate the loop
notifications =[0,0,1,1,1,0,0]

#0 --> notification read
#1 --> unread notification
#notification checker
for notification in notifications:
    #you need to map a condition
    if notification ==1:
        print("unread notification")
        break #it exits early,the else block will be skipped
else:
    print("all notifications are caught up")
#print("all notifications are caught up")
==============================
#searching in a list
#you want to handle the "item not found" case

fruits = ['apple','kiwi','grapes','banana']
item = input('which fruit u want:').lower()
for fruit in fruits:
    if item == fruit:
        print(f'you got your desired {item}')
        break
else:
    print(f'could not find the {item} in the fruits')
========================================
#continue --> will skip the current iteration and proceeds for the rmng iteration

fruits = ['apple','kiwi','grapes','banana']
item = input('which fruit u want:').lower()
for fruit in fruits:
    if item == fruit:
        print(f'you got your desired {item}')
        continue
else:
    print(f'could not find the {item} in the fruits')

============================
notifications = list(map(int,input("enter the value:").split(',')))
print(notifications)
#0 --> notification read
#1 --> unread notification
#notification checker
for notification in notifications:
    #you need to map a condition
    if notification ==1:
        #pass it is mainly used as a placeholder
        print("unread notification")
        continue
else:
    print("all notifications are caught up")


#while ---> loops -->it is mainly used when we rely condition,it will be completly executed until the conditionis satisfied
while<condition>:
      statement(s)...
      ............

while True:
    print("yes") # it runs an infinite loop we need to keyboard interrupt



i = 0
while i<=10:
    print(i)
    i = i+1
    print(i)

    
i = 10
while i>=1:
    print(i)
    i = i-1 #decrement
'''
i = 1
while i<=10:
    print(10-i)
    i = i+1














