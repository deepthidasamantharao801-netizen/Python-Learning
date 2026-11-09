
star pyramid pattern:

n = int(input('enter the value:'))
for i in range(1,n+1):
    for j in range(1,n+1):
        if j<=n-i:
            print(" ",end = "")
        else:
            print("*",end = " ")
    print()

n = int(input('enter the value:'))
#upper part
for i in range(n):
    print(" "*(n-i-1)+"* "*(i+1))
#lower part
for i in range(n-1,0,-1):
    print(" "*(n-i-1)+"* "*(i+1))
































