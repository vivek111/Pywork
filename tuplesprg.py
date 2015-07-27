import collections
sale=collections.namedtuple("Sale","productid","csid","date",qty,price)
sales=[]
sales.append(sale("2","3","5","3-10-15",7,78))
sales.append(sale("3","5","6","8-6-12",8,67))  

tot=0

for sale in sales:
    tot=tot+sale.qty*sale.price
print("Total=",tot)    
