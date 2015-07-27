print("m<n,Where m and n are even")
m=int(input("Enter the lower range\n"))
n=int(input("Enter the upper range\n"))

for i in reversed(range(m,n+1)):
    if i%2==0:
        print(i)
       
    
