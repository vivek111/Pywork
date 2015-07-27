import collections
student=collections.namedtuple("student","name usn dob s1 s2 s3 s4 s5 percent")
n=int(input("enter the number of students to be added"))
p=0
students=[]
while p<n:
  print("enter the details of student\t ",p+1)
  name1=input("enter the name of the student\t")
  usn1=input("enter the usn\t")
  dob1=input("enter the date of the birth in the format d-m-y\t")
  s11=int(input("enter the marks in subject1\t"))
  s12=int(input("enter the marks in subject2\t"))
  s13=int(input("enter the marks in subject3\t"))
  s14=int(input("enter the marks in subject4\t"))
  s15=int(input("enter the marks in subject5\t"))
  total=s11+s12+s13+s14+s15
  p1=(total/500)*100
  
  students.append(student(name1,usn1,dob1,s11,s12,s13,s14,s15,p1))
  p=p+1
p=0
for student in students:
    print("the details of student",p+1,"\n")
    print("name:",student.name,"\n")
    print("usn:",student.usn,"\n")
    print("dob:",student.dob,"\n")
    print("marks in subject1:",student.s1,"\n")
    print("marks in subject2:",student.s2,"\n")
    print("marks in subject3:",student.s3,"\n")
    print("marks in subject4:",student.s4,"\n")
    print("marks in subject5:",student.s5,"\n")
    print("percent:",student.percent)
    p=p+1
    

hi=students[0]
for student in students:
   if (hi.percent<student.percent):
      hi=student
print("student who as scored highest marks is ",hi.name,"marks=",hi.percent)
      

  
  
  
  

