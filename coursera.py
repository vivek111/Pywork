while True:
    x=input("Enter a number\n")
    if(x=="done"):
        break
    if(x==""):
        break
    try:
        x=float(x)
    except:
        print("Invalid Input")
        continue 
    largest=x     
    x=input("Enter a number\n")  
    if(x=="done"):
        break
    if(x==""):
        break
    try:
        x=float(x)
    except:
        print("Invalid Input")
        continue 
    smallest=x
    if largest<smallest:
        temp=largest
        largest=smallest
        smallest=temp
    print("Maximum is",largest)
    print("Minimum is",smallest)                     
