import random
import sys

if len(sys.argv)<2:
    print("Insufficient arguments")
    exit()
else:    
    articles = ["the", "a", "another", "her", "his"]
    subjects = ["cat", "dog", "horse", "man", "woman", "boy", "girl"]
    verbs = ["sang", "ran", "jumped", "said", "fought", "swam", "saw",
         "heard", "felt", "slept", "hopped", "hoped", "cried",
         "laughed", "walked"]
    adverbs = ["loudly", "quietly", "quickly", "slowly", "well", "badly",
           "rudely", "politely"]
    x=int(sys.argv[1])    
    file1=open("firstfile.txt","a+")
    for w in range(0,x):
        z=random.choice(articles)
        z=z+" "+random.choice(subjects)
        z+=" "+random.choice(verbs)
        k=random.randint(0,1)
        if k==1:
            z+=" "+random.choice(adverbs)+"\n"
        else:
            z=z+"\n"
        file1.write(z)
    file1.close()      
    
    file1=open("firstfile.txt","r")
    for line in file1:
        line=line.upper()
        print(line)      
    
    file1.close()    
    

                
            

               
      
