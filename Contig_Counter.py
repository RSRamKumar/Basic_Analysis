########### This code produces the list of contigs already present in the multi fasta file, It also identifies the list of contigs that are not present in the file##########
X=[]
X_1=[]
import re
f1=open("C:/Users/AMRF4/Desktop/Ram Kumar/Blast/BK6.fas","r")
for line in f1:
    #print(line)
   # x=re.findall(r'Query= SO_3590_38529_R1_(paired)_trimmed_(paired)_cogtig_(\d{1,2,3})',line)
    #x=re.findall(r'Query=\s?SO_\d{4}_\d{4}_R1_(paired)_trimmed_(paired)_cogtig_\d{1,2,3}',line)
    #x=re.findall(r'Lambda\s+[A-Z]\s+[A-Z]',line)
    x=re.findall(r'contig_\d+',line)
    #y=re.findall(r'\d{2,3}',X_1)
    if len(x) != 0:
        X.append(x)
for sublist in X:
    for item in sublist:
        X_1.append(item)
A=[]
import re
for i in X_1:
    a=re.sub('contig_',' ',i)
    A.append(a)
found_contigs=[]    
for i in range(0,len(A)):
    found_contigs.append(int(A[i]))
found_contigs.sort()
#print(set(B))

S=set([i for i in range(1,found_contigs[-1]+1,1)])
Not_found_contigs= set(S)-set(found_contigs)
print('The contigs that are not found:')
print(Not_found_contigs)
print('The last count of the contig is',found_contigs[-1])
print('The no. of available contigs is',len(found_contigs))

"""
Intution:
In a multi fasta file, the contigs are numbered in a continuous fashion.
Eg: contig_1, contig_2, contig_3 ....
This code identifies the contigs presents in a multi fasta file and also the missing contigs that may be removed because of impurity.

"""
