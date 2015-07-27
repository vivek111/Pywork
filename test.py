import string
import sys

words={}
#An Empty Dictionary is created
stripseq=string.whitespace + string.punctuation + string.digits + "\"'"#used to remove any other characters
for filename in sys.argv[1:]:#for any no of files
    for line in open(filename):#opens in read mode by default
    #line is a single line and for for loop it is a sequence of lines
        for word in line.lower().split():#
            word = word.strip(stripseq)#to stripe of all other characters
            if len(word)>2:
                words[word] = words.get(word,0) + 1#if word has occured previously it givs prvs vaue
                #else it gives default value as 0.To this count we r adding 1
                
for word in sorted(words):#sort the keys in alphabetical order
    print("'{0}' occurs {1} times".format(word, words[word]))
    #0-positional parameter,

#print(words)
    
    
    #if word not in words:
    #   words[word] = 0
    #words[word] += 1
