import random

x=int(input("Enter the no of rows"))
y=int(input("Enter the no of columns"))
p=int(input("Enter minimum value"))
q=int(input("Enter max value"))
m=x
r=y
while m>0:
    q=''
    r=y
    while r>0:       
        z=random.randint(p,q)
        x=str(z)
        q=q+x+"          "
        r=r-1
    print(q)
    m=m-1
    
