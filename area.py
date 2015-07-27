import math
def triarea(a,b,c):
    """Triangle area calculation"""
    s=(a+b+c)/2 
    ar=math.sqrt(s*(s-a)*(s-b)*(s-c))
    return ar
x=int(input("Enter side 1\n"))
y=int(input("Enter side 2\n"))
z=int(input("Enter side 3\n"))
area=triarea(x,y,z)
print("Area of the triangle=",area)    
