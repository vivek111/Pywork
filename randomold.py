import random

x=int(input("Enter the no of rows"))
y=int(input("Enter the no of columns"))
p=int(input("Enter minimum value"))
q=int(input("Enter max value"))

h=x*y

while h>0:       
    z=(random.randint(p,q))
    print(z,"          ")
    h=h-1
