import os 
from functools import reduce

os.chdir(r'C:\Users\Ram Kumar R S\Desktop\scripts\New folder (2)\new')
import re
for file in os.listdir():
    fin= open(file,'r') 
    X=[] 
    X_1=[]
    f=[]
    for l in fin:
        f.append(l)
        x=re.findall(r'contig_\d+',l)
        if len(x)!=0:
                X.append(x)
    X_1=reduce(lambda x,y: x+y,X)  # list flattening
    fin.close()  # removes the permission error
    #j=re.sub('cogtig','contig',j)
    for n in X_1:
        name=n+'_genbank.txt'
    os.rename(file,name)  # renames the old file with new ones
   
   
   # This code renames the list of genbank files in a given directory based on the given identifier present inside the file.
   # Here "contig_" number is used.
   """
   Input:
   A.txt
   B.txt
   Output:
   contig_54_genbank.txt
   contig_12_genbank.txt
