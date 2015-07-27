import  sys
count=1
for arg in sys.argv:
    print(count,":",arg)
    count=count+1
print("The no of commandline argumnets is %d"%(len(sys.argv)))    

