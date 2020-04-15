input=[]   
f1=open('stem.txt','r')  
for i in f1:
    input.append(i.strip('\n').upper())
    
    
from Bio import SeqIO
for record in SeqIO.parse('Pseudomonas_aeruginosa_PAO1_107_intergenic.fasta', 'fasta'):
         A[record.description]=str(record.seq) 
         
         
         
key_list = list(A.keys()) 
val_list = list(A.values()) 
  
f3=open('only_intergenic+RHOseq.txt','w')
for i in input:
    #print(i)
    for j in A.values():
        #print(j)
        if i in j:
            index=key_list[val_list.index(j)]
            #f3.write('{}\n{}\n{}\n\n'.format(i, index,j))
            f3.write('{}\n{}\n'.format(index,j))
# This code is performing simplified BLAST. Given a list of query sequence, it identifies that sequences in a fasta file and writes in 
#a csv file, in the format of the query in the first line, the found entire length seqence in the second line.
