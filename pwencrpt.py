#list= [('a','m'), ('b','o'), ('c','q'), ('d','s'), ('e','u'), ('f','w'), ('g','y')]
print("a,b,c,d,e,f,g")
pasword=input("Enter the password using above alphabets\n")
temp=pasword
pwlist=[]
encrpt=tuple()

x=0
while x<len(temp):
    if temp[x]=='a':
        encrpt=(temp[x],'m')
    elif temp[x]=='b':
        encrpt=(temp[x],'o')
    elif temp[x]=='c':
        encrpt=(temp[x],'q')
    elif temp[x]=='d':
         encrpt=(temp[x],'s')
    elif temp[x]=='e':
        encrpt=(temp[x],'u')
    elif temp[x]=='f':
         encrpt=(temp[x],'w')
    elif temp[x]=='g':
          encrpt=(temp[x],'y')
    pwlist.append(encrpt)      
    x=x+1  
    
print("Encrypted password is\n")
print(pwlist)        

print("m,o,q,s,u,w,y")
temp=input("Enter the Encrypted password using above alphabets\n") 

pwlist=[]
x=0
while x<len(temp):
    if temp[x]=='m':
        encrpt=(temp[x],'a')
    elif temp[x]=='o':
        encrpt=(temp[x],'b')
    elif temp[x]=='q':
        encrpt=(temp[x],'c')
    elif temp[x]=='s':
         encrpt=(temp[x],'d')
    elif temp[x]=='u':
        encrpt=(temp[x],'e')
    elif temp[x]=='w':
         encrpt=(temp[x],'f')
    elif temp[x]=='y':
          encrpt=(temp[x],'g')
    pwlist.append(encrpt)      
    x=x+1   
    
print("Decrypted password is\n")
print(pwlist)      
