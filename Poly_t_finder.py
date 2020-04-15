from functools import reduce
import re
X=[]
X_1=[]
f1=open(r'C:\Users\Ram Kumar R S\Desktop\sample.txt','r')
for line in f1:
    m=re.findall(r'[,0-9]+[actg]+t{4,}$',line)
    if len(m) != 0:
        X.append(m)
        

        
X_1=list(reduce(lambda x,y: x+y,X))  # list flattening


f2=open(r'C:\Users\Ram Kumar R S\Desktop\sample_out.txt','w')        
for i in X_1:
    a=i.split(',')[0]
    b=i.split(',')[1]
    c=i.split(',')[2]
    d=i.split(',')[3]
    f2.write('{},{},{},{}\n'.format(a,b,c,d))
    
    
# This code identifies poly-t sequence when an input containing start,stop,len,sequence is given. ####
#The sample input is shown, the output is written fetching only the rows having poly t in the tail sequence the condition is mentioned above
#5,154,786,atactagatactagaataatactattactttttttttttttacttttttactttttttttttttttttttttttt
#15,154,786,atactagatactagaataatactattacttgatttt
#25,154,786,atactagatactagaataatactattac
#30,154,786,atactagatactagaataatactattactatatactagactaactactactactacatagatacaatttt
#40,154,786,atactagatactagaataa
#45,154,786,atactagatactagaataatactatt

######### Different other versions of presence of poly-t in a sequence####
# m=re.findall(r'[t{4,}[actg]+]',line)
#m=re.findall(r'[t{4,}[actg]{4} | [actg]{4}t{4,}$]',line)
#m=re.findall(r'[actg]+t{4,}',r)
#i=re.findall(r't{4,}[actg]{10}',r)
