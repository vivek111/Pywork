def leapyr(leaps):
    for year in range(1980,2020):
        if(year%4==0 and year%100!=0) or (year%400==0):
            leaps.append(year)
    return 
            
leaps=[]
leapyr(leaps)
print("Leap years are")
print(leaps)            
