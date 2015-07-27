def month(n,x):
	month=list()
	i=1
	for k in range(0,x):
	    month.append("")
	while True:
		month.append(i)
		i+=1
		if i>29 and n==29:
			rem=7
			break
		month.append(i)
		i+=1
		if i>30 and n==30:
			rem=6
			break
		month.append(i)
		i+=1
		if i>31 and n==31:
			rem=5
			break
		month.append(i)
		i+=1
		month.append(i)
		i+=1
		month.append(i)
		i+=1
		month.append(i)
		i+=1
		if i>28 and n==28:
			rem=8
			break
	for i in range(n,n+rem+10):
		month.append("")
	return month

while True:
    n=int(input("Enter the no of days in a month\n"))
    if n>31 or n<28:    
        print("Invalid no of days\n")
    else:
        break   
x=int(input("Enter the day (1<day<7)\n"))            
k=list()
k=month(n,x)

print("Su\tMon\tTue\tWed\tThu\tFri\tSat")
j=0
for i in range(0,6):
	print(str(k[j])+"\t"+str(k[j+1])+"\t"+str(k[j+2])+"\t"+str(k[j+3])+"\t"+str(k[j+4])+"\t"+str(k[j+5])+"\t"+str(k[j+6]))
	j=j+7
	i=i+1

	
		
	
