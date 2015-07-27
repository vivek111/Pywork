cric=set()
football=set()
hockey=set()

x=int(input("Enter the no of students\n"))
for i in range(0,x):
    name=input("Enter your name\n")
    print("Are you interested in Cricket\n")
    k=input("Press Y or N")
    if k=='Y' or k=='y':
        cric.add(name)
    print("Are you interested in football\n")   
    k=input("Press Y or N")
    if k=='Y' or k=='y':
         football.add(name) 
    print("Are you interested in Hockey\n")   
    k=input("Press Y or N")
    if k=='Y' or k=='y':
         hockey.add(name) 

print("Students who play Cricket\n")
print(cric)
print("Students who play Football\n")
print(football)   
print("Students who play Hockey\n")
print(hockey)  

both=set()
both=cric&football
print("Students who play both cricket and football")
print(both)  
     
      
         

    
    
    
    
    
    
