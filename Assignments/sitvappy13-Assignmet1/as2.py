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
    k=random.randint(0,1)
    for w in range(0,x):
        z=random.choice(articles)
        z=z+" "+random.choice(subjects)
        z+=" "+random.choice(verbs)
        if k==1:
            z+=" "+random.choice(adverbs)
            print(z)    
        else:
            print(z)
               
      
