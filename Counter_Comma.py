####### This code counts the number of entries in a single row  present in each line of a file#######
targets=[]
f1=open('tar_only.csv','r')
for i in f1:    
    targets.append(i)
a =[]
def split (l):
    for i in range (0, len (l)):
        if ',' in l[i]:
            a.append ((len (l[i].split (',')))) 
        else:
            a.append(0)
            
         
    return (a) 
k = split (targets)
#print (k)
print(a)
f2=open('tar_count.csv','w')
for i in a:
    f2.write("%s\n" %i)
"""Sample Content Present in the file is a file in which each row has values separated by a delimiter. 
s='leuC,surA , spuF,PA2408,PA0383 ,PA0475 ,oprD, infB ,pcaQ ,trpC ,ldcA ,ponA,phaF, czcB , pscD,xseB,acoB'
    
print(len(s.split(',')))"""
