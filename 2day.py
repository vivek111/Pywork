
import time
ct=5
print("I am count down timer")
while ct>0:
	print("It is %d"%(ct))
	time.sleep(2)
	ct=ct-1
print("Boom")

states=["book","pencil","pen","table","chair"]
ct=1
for state in states:
        print(ct,state)
        ct=ct+1
