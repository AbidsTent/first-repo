"""c= dictionary(...)
print(sorted([(v,k) for k,v in c.items()]))"""

name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
fh = open(name)
dix={}
for line in fh:
    if not line.startswith("From "):
        continue
    line= line.rstrip().split()
    hr=line[5].split(":")[0]
    dix[hr]=dix.get(hr,0)+1
print(dix)
for kei,val in sorted([(k,v) for k,v in dix.items()]):
    print(kei,val)