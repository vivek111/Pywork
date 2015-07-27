def dollarsToRupees(x, rate = 63.53)
    valInRs  = x*rate;
    return valInRs
    
val = dollarsToRupees(25)
print("%d dollars = %f rupees" %(25,val))
val = dollarsToRupees(25, 64.34)
print("%d dollars = %f rupees" %(25,val))


def badFn(a, b=1, c)


def shorten(text, length=15, indicator="...")
    if len(text) > length
        text = text[:length -len(indicator)] + indicator
    return text


print(shorten("The road to hell is here"))
print(shorten("All roads lead nowhere", length = 10))
print(shorten(length = 8, text ="Whats goes up"))
print(shorten("Watched Pot never boils", 9, "*"))



Naming Conventions


uppercase - constants
Titlecase - classes, exceptions
camelcase - functions

Parameter unpacking
#keyword arguments
def sum_of_powers(*args, power=1):
    result =0
    for arg in args:
        result += arg ** power
    return result
    
sum_of_powers(1,3,5)
sum_of_powers(1,3,5,power=2)
sum_of_powers(1,3,5,2)

def triArea(a,b,c,*,units = "square meters")
    """ Triangle area calculation"""
    s = (a+b+c)/2
    area = math.sqrt(s*(s-a)*(s-b)*(s-c))
    return "{0} {1}".format(area, units)
    
triArea(25,24,7)
triArea(41, 9,40, units = "square kms")
triArea(25,24,7, "sqaure inches")           #


* at first - no positional parameters

def print_setup(*, paper = "A4", copies = 1, color = False)

print_setup(paper = "Letter", color = True)
print_setup("A3")           #error







unpack mappings using *

options = dict(paper = "A4", color = True)
print_setup(**options)

def add_person_details(ssn, surname, **kwargs)
    print("SSN = ", ssn)
    print("surname = ", surname)
    for key in sorted(kwargs):
        print("{0} = {1}".format(key, kwargs[key]))
        

def area(b,h)
    return b*h/2

area = lambda b, h: 0.5*b*h

area(9,8)



#no iterations or branch or return statement

s = lambda x: "" if x == 1 else "s"

print("{0} file{1} processed".format(count, s(count)))

assert boolean_expression, optional_expression

def product(*args):
    assert all(args), "0 value arguments"
    result = 1
    for arg in args:
        result *= arg
    return result
    
    
    

def product(*args):
    result = 1
    for arg in args:
        result *= arg
    assert result, "0 value arguments"
    return result
    
    
    
    
   
