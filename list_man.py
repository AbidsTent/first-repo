"""fname = input("Enter file name: ")
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
"""
fname = input("Enter file name: ")
try:
    fh= open(fname)
except:
    print("Not found:",fname)
    quit()
count = 0
for line in fh:
    if not line.startswith("From "):
        continue
    line = line.rstrip()
    line=line.split()
    print(line[1])
    count+=1

print("There were", count, "lines in the file with From as the first word")
