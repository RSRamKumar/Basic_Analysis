c=1
from Bio import SeqIO
for record in SeqIO.parse(r'C:\Users\Ram Kumar R S\Downloads\sequence.fasta', "fasta"):
    with open(r'C:\Users\Ram Kumar R S\Downloads\fasta_'+str(c)+'.txt','w') as f:
        f.write('{}\n{}\n'.format(record.id,record.seq))
        c=c+1
      
  # This code is for splitting the individual fasta records in a multi fasta file and write them to separate files.
  """
  Input:
  >NW_006890304.1:c509009-1 Callorhinchus milii isolate IMCB2004 unplaced genomic scaffold, Callorhinchus_milii-6.1.3 scaffold_251, whole genome shotgun sequence
TTTTAAACGCCTCAATTAGATCGCGCTTTAACCCGCTCTGTTCTAAGGAATACAATCTAAGTCTTCCCAG
CCCACAAAATTTACAGTTGGTTGACATTACAGTGTATTCTGTGAAGCGCTTTGGAACGTCTCGAAGATGT

>Sample Check  Callorhinchus milii isolate IMCB2004 unplaced genomic scaffold, Callorhinchus_milii-6.1.3 scaffold_251, whole genome shotgun sequence
TTTTAAACGCCTCAATTAGATCGCGCTTTAACCCGCTCTGTTCTAAGGAATACAATCTAAGTCTTCCCAG
CCCACAAAATTTACAGTTGGTTGACATTACAGTGTATTCTGTGAAGCGCTTTGGAACGTCTCGAAGATGT
GATTATCATCAGAGCAAATCCCTTCATTCCCCGATAAATGCAATAAAACTCGCACATATCCGTCGGGAGC

Ouput:
creation of 2 fasta files each containing individual fasta records :
fasta_1.txt
fasta_2.txt
"""
