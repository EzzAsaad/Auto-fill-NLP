# -*- coding: utf-8 -*-
"""
Created on Wed Mar  4 19:33:33 2020

@author: Kase
"""
import nltk
#nltk.download()
import re
from collections import Counter


def trigramfunction(tokens,n=3):
    temp = []
    tokens = iter(tokens)
    while n > 1:
        try:
            nextword = next(tokens)
        except StopIteration:
            return
        temp.append(nextword) 
        n -= 1
    for token in tokens:
        temp.append(token)
        yield(tuple(temp))
        del temp[0]
string =""
read = open("data.txt","r",encoding="UTF-8")
string += re.sub(r"[\W]", ' ', str(read.readlines()))
read.close()
words_tokens = nltk.word_tokenize(string)
#tuples = list(nltk.trigrams(words_tokens))
tuples = list(trigramfunction(words_tokens))



a,b,c = list(zip(*tuples))
bgs = list(zip(a,b))

counter = Counter(bgs)

counterr = Counter(tuples)

tDuo={str(("","")):0}
tTri={str(("","","")):0}
 
TRIOBJ={str(("","")):[]} 

clock = 0
for i in tuples:
    w0,w1,w2=i
    bgss = (w0,w1)
    
    if str(bgss) not in TRIOBJ.keys() and str(bgss) not in tDuo.keys():
        counter1=counter[bgss]
        counter2=counterr[(w0,w1,w2)]
        prob = round(counter2/counter1,3)
        
        TRIOBJ.__setitem__(str((w0,w1)),[(w2,prob)])
        
        tDuo.__setitem__(str((w0,w1)),counter1)
        tTri.__setitem__(str((w0,w1,w2)),counter2)

    else:
        if (w0,w1,w2) in tTri.keys():
            prob = round(tTri[(w0,w1,w2)]/tDuo[bgss],3)

            TRIOBJ[str(bgss)].append((w2,prob))
        else:
            counter2=counterr[(w0,w1,w2)]
            prob = round(counter2/tDuo[str(bgss)],3)         
            TRIOBJ[str(bgss)].append((w2,prob))
            tTri.__setitem__(str((w0,w1,w2)),counter2)
    temp = []
    

            
Entered_Word1 = input("Enter Your Word1:")
Entered_Word2 = input("Enter Your Word2:")

#print(str(TRIOBJ["('الثمانية', 'حيث')"]))

if str((Entered_Word1,Entered_Word2)) in TRIOBJ.keys():
    print(str())
    CommonWords= Counter(TRIOBJ[str((Entered_Word1,Entered_Word2))])
    if len(CommonWords) >= 2:
        MCW = CommonWords.most_common(2)
        words,digits = MCW[0]
        print(words[0]+" "+str(words[1]))
        words,digits = MCW[1]
        print(words[0]+" "+str(words[1]))
    else:
        MCW = CommonWords.most_common()
        words,digits = MCW[0]
        print(words[0]+" "+str(words[1]))
    
else:
    mostcommon = counter.most_common(1)
    words,digits = mostcommon[0]
    CommonWords= Counter(TRIOBJ[str(words)])
    if len(CommonWords) >= 2:
        MCW = CommonWords.most_common(2)
        words,digits = MCW[0]
        print(words[0])
        words,digits = MCW[1]
        print(words[0])
    else:
        MCW = CommonWords.most_common()
        words,digits = MCW[0]
        print(words[0])