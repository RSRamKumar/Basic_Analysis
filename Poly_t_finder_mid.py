f1=open('interregion1.csv','r')
f2=open('midregion.csv','w')
for line in f1:
    i=line.split(',')[0]  # start
    j=line.split(',')[1]  # stop
    a=line.split(',')[2]  # length
    m=int(a)/2
    m1=round(m)           # find the mid length of the sequence
    b=line.split(',')[3]   
    seq=b[int(m1):]       # sequence extraction from the mid length
    f2.write('{},{},{},{},{}'.format(i,j,a,m1,seq))  # write in output file
    
    
    
import re
X=[]
X_1=[]
f1=open('interregion.csv','r')
for line in f1:
    #m=re.findall(r'[,0-9]+[actg]+t{5,}[actg]+',line)           # Different conditions of Regex
    #m=re.findall(r'[,0-9]+[[actg]+t{4,}[actg]+|t{4,}$]',line)
    #m=re.findall(r'[,0-9]+[actg]+t{4,}$',line)
    #m=re.findall(r'[,0-9]+[[actg]+t{4,}|t{4,}$]',line)
   
       if len(m) != 0:
        X.append(m)
        
for sublist in X:
    for item in sublist:
        X_1.append(item)

f3=open('poly.csv','w')          # write in output file
for i in X_1:
    a=i.split(',')[0]
    b=i.split(',')[1]
    c=i.split(',')[2]
    d=i.split(',')[3]
    #e=i.split(',')[4]
    f3.write('{},{},{},{}\n'.format(a,b,c,d))
    #f3.write('{}\n'.format(d))
    
    
    # This code identifies poly-t sequence from the mid regin of a sequence when an input containing start,stop,len,sequence is given. ####
