D={ 
'list1':['aaa','bbb','ccc','eee','kkk'],
'list2':['bbb','aaa','ggg','nnn'],
'list3':[],
'list4':['zzz']
}
comp=['aaa', 'ccc', 'nnn', 'eee', 'kkk', 'ggg', 'bbb']
key={}
for k,v in D.items():
   # A={i:'+' for i in v if i in comp}
    A={i:'+' for i in v }
    key[k]=A
    
    

import pandas as pd
final=pd.DataFrame(key)
final.fillna('-',inplace=True)
print(final)

""""
    list1 list2 list3 list4
aaa     +     +     -     -
bbb     +     +     -     -
ccc     +     -     -     -
eee     +     -     -     -
ggg     -     +     -     -
kkk     +     -     -     -
nnn     -     +     -     -
zzz     -     -     -     +

[8 rows x 4 columns]
""""

