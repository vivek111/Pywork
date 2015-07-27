def product(*args):
    result=1
    for arg in args:
        result*=arg
    return result
    
print(product(1,3,5,7))
t=(1,3,5,7)
print(product(*t))
print(product(*range(11,15)))        
    
