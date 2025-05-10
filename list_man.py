fname = input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
    line=line.rstrip()
    #print(line)
    lis= line.split()
    for i in lis:
        if i not in lst:
            #print(i)
            lst.append(i)
    #print(lst)
    
lst.sort()
print(lst)
