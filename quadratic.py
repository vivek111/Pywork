import math
a=input("Enter the value of a\n")
a=float(a)
b=input("Enter the value of b\n")
b=float(b)
c=input("Enter the value of c\n")
c=float(c)

if a==0:
	print("Not a quadratic equation")
else:
	x=(b*b)-(4*a*c)

	if x>0:
		print("Roots are real and distinct")
		p=(-b+(math.sqrt(x))/(2*a))
		p="{0:12.6f}".format(p)
		q=(-b-(math.sqrt(x))/(2*a))
		q="{0:12.4f}".format(q)
		print("Root1=",p,"\nRoot2=",q)
	elif x==0:
		print("Roots are real and equal")
		p=-(b/(2*a))
		q=p
		print("Root1=",p,"\nRoot2=",q)
	else:
		print("Roots are imaginary")
		p=-(b/(2*a))
		q=math.sqrt(-x)/(2*a)
		print("Root1=",p,"+",q,"i")
		print("Root2=",p,"-",q,"i")


