#Write a program which accepts a number n between 1 and 100 from the user and displays all numbers between 1 and #1000 not divisible by n.
number=[]
while True:
    x=int(input("Enter any integer b/w 1 and 100\n"))
    if x>=1 and x<=100:
        break
for w in range(0,1000): 
    if w%x!=0:
        number.append(w)
    else:
        j=0    
    w=w+1
print(number)            
              
