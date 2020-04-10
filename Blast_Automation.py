X=[]
Y=[]

from functools import reduce
import re
f1=open(r"C:\Users\Ram Kumar R S\Downloads\911ZZ6GT016-Alignment.txt","r")  
for line in f1:
    x=re.findall(r'Query\s+\d+\s*([A-Za-z|-]+)',line)
    y=re.findall(r'Sbjct\s+\d+\s*([A-Za-z|-]+)',line)
    if len(x) != 0:
        X.append(x)
    if len(y) != 0:
        Y.append(y)
    
Q=''.join(reduce(lambda x,y: x+y,X))  # list flattening
S=''.join(reduce(lambda x,y: x+y,Y))

l=[]       
for i in range(0,len(Q)):
     if Q[i]!=S[i]:
         s=Q[i]+str(i+1)+S[i]
         l.append(s)
str1 = ','.join(l)     
   
#Reference:https://stackoverflow.com/questions/952914/how-to-make-a-flat-list-out-of-list-of-lists
