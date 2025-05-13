"""fname = input ("Enter file name: ")
try:
    fh = open (fname)
except:
    print("File not found: ",fname)
    quit()
dix = {}
count=0
for line in fh:
    for word in line.split(", "):
        count+=1
        if word in dix:
            dix[word] += 1
        else:
            dix[word] = 1
print(dix)
print (count)
for k,v in dix.items():
    print("Name:",k,"Times:",v)"""

name = input("Enter file:") or "mbox-short.txt"
try:
    fh= open(name)
except:
    print("Wrong file name.")
    quit()
dix={}
for line in fh:
    if not line.startswith("From "):
        continue
    else:
        words=line.rstrip().split()
        dix[words[1]]=dix.get(words[1],0)+1
print(dix)
most=0
keyy=None
for k,v in dix.items():
    if v>most :
        most = v
        keyy = k
print(keyy,most)
        
        
