"""
h = input("Enter Hours:")
r = input("Enter rate:")
try:
    h = float(h)
    r = float(r)
except:
    print("Error: Invalid input")
    quit()
print(h,r)
rem = h-40

if rem>0 :
    base = 40*r
    r= r*1.5
    ex = rem*r
    print(base+ex)
else:
    print(h*r)
score = input("Enter:")
try:
    scr= float(score)
except:
    print("Error: Invalid input")
    quit()
if scr>=0.0 and scr<=1.0:
    if scr>= 0.9:
        print("A")
    elif scr>= 0.8 :
        print("B")
    elif scr>= 0.7 :
        print("C")
    elif scr>= 0.6 :
        print("D")
    elif scr< 0.6 :
        print("F")
else: 
    print("Error: Invalid input")

def computepay(h, r):
    rem = h-40
    if rem>0 :
        base = 40*r
        r= r*1.5
        ex = rem*r
        return base+ex
    else:
        return h*r

hrs = input("Enter Hours:")
h=float(hrs)
rate = input("Enter rate:")
r=float(rate)
p = computepay(h, r)
print("Pay", p)
largest = None
smallest = None
while True:
    num = input("Enter a number: ")
    if num == "done":
        break
    try:
        num = int(num)
    except:
        print("Invalid input")
        continue
    if smallest is None:
        smallest = num
    if largest is None:
        largest = num
    if num>largest:
        largest = num
    if num<smallest:
        smallest = num

print("Maximum is", largest)
print("Minimum is", smallest)
"""

