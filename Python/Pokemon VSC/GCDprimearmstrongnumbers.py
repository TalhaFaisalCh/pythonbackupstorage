a, b = map(int, input('enter 2 numbers: ').split())
limit = False
if a > b:
    x = a
else:
    x = b
def GCP(a, b, x):
    c,d,Z=a,b,0
    for i in range(x):
        c /= i+1
        d /=  i+1
        if c == int(c) and d == int(d):
            Z = i
        c,d=a,b
    return Z+1

def GCP2(a, b, x):
    for i in range(x, 2, -1):
        if a % i == 0 and b % i == 0:
            return i
    return 1 

GCPfinder = GCP2(a, b, x)
print(GCPfinder)


def prime(x):
    for i in range(2,x):
        if x % i == 0 and x != i:
            return False
    return True

for x in range(1, 100):
    if prime(x):
        print(x)
    


def armstrong(r):
    r = str(r)
    l, t = len(r), 0
    for i in range(l):
        t += int(r[i])**l
    return t
for r in range(1000, 20000):
    if armstrong(r) == r:
        print(r)