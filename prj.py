import collections
student=collections.namedtuple("nameusndob","m1m2m3m4m5","perc")
print("                     Students Records            ")
x=input("Enter the no of students for which operations has to be done\n")
x=int(x)
record=[]

for k in range(0,x):
    name1=input("Enter the name\n")
    usn1=input("Enter the usn\n")
    dob1=input("Enter date of birth in dd-mm-yy\n")
    print("Enter the marks in 5 subjects\n")
    s1=input()
    s2=input()
    s3=input()
    s4=input()
    s5=input()
    p=(int(s1)+int(s2)+int(s3)+int(s4)+int(s5))/5
    record .append(student(name1,usn1,dob1,s1,s2,s3,s4,s5,p))
    
    

