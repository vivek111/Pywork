target = 66
while True :
    while True:
	    value = input("Enter an integer between 1 and 100\n")
	    try:
		    value = int(value)
		    break
	    except ValueError:
		    print("I said enter an integer!")
		
    if value > target:
	    print (value, "is too high")
    elif int(value) < target:
	    print("too low")
    else:
	    print("Perfect")
	    break

