#We define twin primes as a pair of prime numbers which differ by 2. Write a program to display the first 25 twin primes.

prime=[]
print
for i in range(1,25):
    j=2
    f=0
    while j<=i:
        if i%j==0:
            f+=1 
        j=j+1
    if f <2:  
        prime.append(i)
    i=i+1
print(prime) 
x=0   
while x<(len(prime)-1):
    if prime[x+1]-prime[x]==2:
        print("(",prime[x],prime[x+1],")")   
    x+=1           
