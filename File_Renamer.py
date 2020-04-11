import os
os.chdir(r'C:\Users\Ram Kumar R S\Downloads\fol')           # Change the directory
for file in os.listdir():
    name,ext=(os.path.splitext(file))                       # split the file name and extension separately
    nam,no=(name.split('_'))                                # split the name if it has any delimiter
    no=no.zfill(2)
    new='{}-{}{}'.format(no,nam,ext)                        # Creation of new file name
    os.rename(file,new)                                     # File Rename Process
    
    
    """
    Input:
    fasta_01.txt
    fasta_02.txt
    
    Output:
    01_fasta.txt
    02_fasta.txt
    """
    # Reference:https://youtu.be/ve2pmm5JqmI
    
