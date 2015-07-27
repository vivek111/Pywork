def extract_from_tag(tag,line):
    opener="<"+tag+">"
    closer="</"+tag+">"
     i=line.find(opener)
     if i!=-1:
        start=i+len(opener)
        j=line.find(closer,start)
        if j!=-1:    
           return line[start:j]
        else:
           break
      else:      
        return None
   
if x!=None:        
    x=extract_from_tag("red","what a <red> rose </red> this is")    
    print(x)        
else:
    print("Not found")    
