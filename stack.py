def push(stack,ele):
    stack.append(ele)
    return

def pop1(stack):
    x=stack.pop()
    return x
    
def display(stack):
    print(stack)
            
stack=[]   
top=-1
size=10         
while True:
    print("1.Push\n2.Pop\n3.Display\n4.Exit")
    x=int(input("Enter your choice\n"))
    if x==1:
        if top==size-1:
            print("stack Full")
        else:    
            ele=int(input("Enter the element to push\n"))
            top+=1
            push(stack,ele)
    elif x==2:
        if top==-1:
            print("Empty stack")
        else:   
            print("Deleted element=",pop1(stack))
            top-=1
    elif x==3:
        if top==-1:
            print("Empty stack")
        else:        
            print("Elements of stack are\n")
            display(stack)
    else: 
        break
                   
        
