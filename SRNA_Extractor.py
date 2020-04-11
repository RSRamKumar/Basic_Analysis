file_name=[]  
import re    
import os
entries = os.listdir('Z:/Ram Kumar/sRNA_CF/3')                              # loop to extract only txt files from the given folder.
for i in entries:
    if i.endswith('.txt'):
        file_name.append(i)
#file_name=['AFXI01.1.txt','AFXJ01.1.txt','AFXK01.1.txt']
for names in file_name:                                                  
    fin=open(names,'r')
    X=[]                                                                    # loop to open the file
    X_1=[]
    l=[]
    for i in fin:
        A=re.findall(r'\Asp[/-a-zA-Z0-9.?\s?/|a-z]+',i)                     # Regex to extract the sRNA - starts with sp and has alphanumeric
        if len(A)>0:
            X.append(A)
    for i in X:
        for j in i:
           X_1.append(j.split('|')[2])
    X_1.sort()
   # print(len(set(X_1)))                                                   # Loop to write in output file - creating file names based on input
    out='sRNA_'+names
    with open(out,'w') as f4:
        [f4.write('{}\n'.format(i)) for i in  set(X_1)]  
        
        
       # Code to extract the sRNA IDs from a number of BLAST result files
