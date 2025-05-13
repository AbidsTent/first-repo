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
    print("Name:",k,"Times:",v)
"""

