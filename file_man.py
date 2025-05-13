"""
fname = input ("Enter file name: ")
try:
    fh = open (fname)
except:
    print("File not found: ",fname)
    quit()
for line in fh:
    line = line.upper()
    print(line.rstrip())
    
"""

fname = input("Enter file name: ")
fh = open(fname)
addr=0
count=0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    #print(line)
    count+=1
    line = line.split()
    num = line[1]
    #print(num)
    addr+=float(num)
ave= addr/count
print("Average spam confidence: ", ave)