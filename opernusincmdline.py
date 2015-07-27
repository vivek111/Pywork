import sys

if(len(sys.argv)<3):
    print("Insufficient arguments")
    exit()
x=int(sys.argv[1])
y=int(sys.argv[2])
if x>y:
    print("%d is greater"%x)
else:
    print("%d is greater"%y)
        
