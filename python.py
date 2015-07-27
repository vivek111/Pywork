x=input("Enter a website\n")
ct=0
vowel="aeiou"
for i in range(len(x)):
	if x[i] in vowel:
		ct=ct+1

print(ct,"/",len(x))
	
