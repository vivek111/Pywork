import random

x=random.randint(0,1)
s="{who} turned {age} this year"
if x==0:
    s=s.format(who="She",age=50)
else:
    s=s.format(who="he",age=40)
print(s)    
