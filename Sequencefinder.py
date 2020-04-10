A={}
seq=[]
from Bio import SeqIO
for record in SeqIO.parse('BK6.fna', 'fasta'):   # Method for reading the Fasta file
    A[record.description]=record.seq             # Appending all the sequence in the seq list
    seq.append(record.seq) 
    
str1 = ''.join(str(e) for e in seq)              # flattening the seq list to combine it as one sequence

out=open('fasta.txt','w')
out.write("{}\n".format(str1))                   # writing the sequence in a output file

A=[]
B=[]
f1=open('Z:/Ram Kumar/BK6/BK6.csv','r')          # file that has the start,stop regions
for i in f1:
    A.append(i.split(',')[0])                    # list A, B contains the initial and final respectively
    B.append(i.split(',')[1].strip('\n'))
    
start=[]
stop=[]                                          # operations to find the intergenic start and stop regions
for i in range(0,len(B)):
    start.append((int(B[i])+1))
    list(set(start))
del(start[-1])
for i in range(1,len(A)):
    stop.append((int(A[i])-1))
    list(set(stop))
    

f3=open('interregion1.csv','w')
for i in range(0,len(start)):
    if start[i] < stop[i]:
        X=str1[start[i]:stop[i]+1]               # Operation to extract the sequence by string splicing
        D=len(X)
        if D  in range(30,551):    
            f3.write("{},{},{},{}\n".format(start[i],stop[i],D,X))
    else:
        X=str1[stop[i]:start[i]+1]
        D=len(X)
        if D  in range(30,551): 
            f3.write("{},{},{},{}\n".format(stop[i],start[i],D,X))
            
            
# This code extracts the intergenic region by reading from a file having start and end coordinates.
# A   B   -------
# 87  95  ------- 96  98
# 99 103  -------104  109
# 110 132 -------
