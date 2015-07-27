import collections
mark=collections.namedtuple("mark","m1 m2 m3 m4 m5 perc")
print("                                                 Students Records            ")
x=input("Enter the no of students\n")
x=int(x)
temp=tuple()
record=[]

k=0
for k in range(0,x):
    print("Student",k+1,"\n")
    name=input("Enter the name\n")
    usn=input("Enter the usn\n")
    dob=input("Enter date of birth in dd-mm-yy\n")
    print("Enter the marks in 5 subjects\n")
    s1=int(input())
    s2=int(input())
    s3=int(input())
    s4=int(input())
    s5=int(input())
    if s1==0 or s2==0 or s3==0 or s4==0 or s5==0:  
        p=0 
    else:    
        p=(s1+s2+s3+s4+s5)/5
    temp=(name,usn,dob,mark(s1,s2,s3,s4,s5,p))
    record.append(temp)

k=0
for k in range(0,x):
     print("Student",k+1,"\n")
    print("\nName:",record[k][0])
    print("USN:",record[k][1])
    print("Date of Birth:",record[k][2])
    if record[k][3].perc==0:
        print("Student",k+1,"is failed")
    else:
        print("Percentage:",record[k][3].perc)
        
        
y=1
p=0
bigper=record[0][3].perc
while y<x:
    if record[y][3].perc>bigper:
        bigper=record[y][3].perc
        p=y
    y+=1 
    
print("\n\n\nStudent having largest percentage:-\n")
print("Name:",record[p][0])
print("USN:",record[p][1])
print("Date of Birth:",record[p][2])
print("Percentage:",record[p][3].perc)
   
    
    
            
        
    
    

