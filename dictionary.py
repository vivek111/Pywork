import os

print("Directory content size:")
content_sizes={name:os.path.getsize(name) for name in os.listdir(".")}#. refers to current directory
for key,val in content_sizes.items():
    print(key,val)
 
 #this part doesnt list directory   
print("File sizes:")
print("=======================")

file_sizes={name:os.path.getsize(name) for name in os.listdir(".") if os.path.isfile(name)}
for key,val in file_sizes.items():
    print(key,val) 
