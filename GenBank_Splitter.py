with open('BK4.gbk', "r") as f:
    buff = []
    i = 1
    for line in f:
        if line.strip():  #skips the empty lines
           buff.append(line)
        if line.strip() == "//":
           output = open('gen_bk'+str(i)+'.txt','w')
           output.write(''.join(buff))
           output.close()
           i+=1
           buff = [] 
           
           
           
        # This code is used to split the given multi genbank files into a number of individual files having named based on the count.
