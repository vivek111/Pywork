product=1
i=iter([1,2,3,4])
while True:
    try:
        product*=next(i)
    except StopIteration:
        break
print(product)          

x=[-2,9,7,-4,3]
print(all(x))
print(any(x))
print(len(x))
print(min(x))
print(max(x))
print(sum(x))
x.append(-6)
print(all(x))
print(any(x))
print(len(x))
print(min(x))
print(max(x))
print(sum(x))
x.append(0)
print(all(x))
print(any(x))
print(len(x))
print(min(x))
print(max(x))
print(sum(x))
