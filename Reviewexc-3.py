"""create a encryption list [('a','m'), ('b','o'), ('c','q'), ('d','s'), ('e','u'), ('f','w'), ('g','y')]

program will ask to enter password
encrypt and show password
later enter encrypted password
decrypt to obtain original password"""

pwlist=[]
print("a,b,c,d,e,f,g")
pasword=input("Enter the password using above alphabets\n")
temp=pasword
encrpt=""

x=0
while x<len(temp):
    if temp[x]=='a':
        encrpt=encrpt+'m'
    elif temp[x]=='b':
       encrpt=encrpt+'o'
    elif temp[x]=='c':
       encrpt=encrpt+'q'
    elif temp[x]=='d':
        encrpt=encrpt+'s'    
    elif temp[x]=='e':
        encrpt=encrpt+'u' 
    elif temp[x]=='f':
        encrpt=encrpt+'w'
    elif temp[x]=='g':
        encrpt=encrpt+'y'
    x=x+1       
        
print("Encrypted password is\n")
print(encrpt)  

print("m,o,q,s,u,w,y")
encrpt=input("Enter the Encrypted password using above alphabets\n")
temp=encrpt 
decrpt=""

x=0
while x<len(temp):
    if temp[x]=='m':
        decrpt=decrpt+'a'
    elif temp[x]=='o':
       decrpt=decrpt+'b'
    elif temp[x]=='q':
       decrpt=decrpt+'c'
    elif temp[x]=='s':
        decrpt=decrpt+'d'    
    elif temp[x]=='u':
        decrpt=decrpt+'e' 
    elif temp[x]=='w':
        decrpt=decrpt+'f'
    elif temp[x]=='y':
        decrpt=decrpt+'g'
    x=x+1          
    
print("\nDecrypted password is\n")  
print(decrpt)     






