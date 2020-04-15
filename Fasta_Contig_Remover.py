######## This code removes the specified contigs from the multi fasta file that are present in input.csv ###########
f1=open('input.csv','r')
inp=[]

for i in f1:
    s='fig|PA39016.peg.'+ i.split(',')[0].strip('\n')   # Altering the name of the contig based on the requirement
    inp.append(s)
remover=inp

A={}
from Bio import SeqIO
for record in SeqIO.parse('PA39016.pep', 'fasta'):    # Fasta file opening
    A[record.description]=record.seq
   

B={} # Required Ones
C={}
  ### Remover ####
for i in A.keys():
    if i not in remover:          # Operation that writes the required one in a separate file and others in a different file
        B[i]=A[i]
    else:
        C[i]=A[i]
with open('PA39016_out.pep', 'w') as f:
    [f.write('>{0}\n{1}\n'.format(key, value)) for key, value in B.items()]
            
with open('PA39016_err.pep', 'w') as f:
    [f.write('>{0}\n{1}\n'.format(key, value)) for key, value in C.items()]     
