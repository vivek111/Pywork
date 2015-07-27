x=[1,2,3,4,5,-6,-5,-8]

i=0
while i<len(x):
    x[i]=abs(x[i])
    i+=1

print(x) 

for i in range(len(x)):
    x[i]=abs(x[i])  
    
print(x)     
