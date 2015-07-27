record="leo tolstoy*1828-8-28*1910-11-20"
x=record.split("*")
y=x[1].split("-")
z=x[2].split("-")

age=int(z[0])-int(y[0])
age=str(age)
print(x[0]+" lived for "+age+" years")
