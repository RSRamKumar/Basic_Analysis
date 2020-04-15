A={}
B={}
C={}
l=[]
seq=[]
from Bio import SeqIO
for record in SeqIO.parse('BSRD.fasta', 'fasta'):
    A[record.description]=record.seq                             
    if len(record.seq) >= 30 and len(record.seq)<=530:        # filtering based on length
        l.append(record)
        B[record.description]=record.seq
    else:
        C[record.description]=record.seq
       
        
with open('filtered_BSRD.fasta', 'w') as f:
    [f.write('>{0},len={1}\n{2}\n'.format(key,len(value),value)) for key,value in B.items()]
        
with open('unfiltered_bsrd.txt', 'w') as f:
    [f.write('>{0},len={1}\n{2}\n'.format(key,len(value),value)) for key, value in C.items()]

output_handle = open("long_seqs.fasta", "w")        
SeqIO.write(l, output_handle, "fasta") # SEQIO way of writing an output file


#### This code is for filtering the fasta file based on the length. #######
