choice = int(input('give length: '))
l = choice
choice = int(input('give breadth: '))
b = choice
for i in range(b):
    print('* ' * l)

choice = int(input('give height for triangle: '))
h = choice
for i in range(h):
    print('* ' * (i+1))

choice = int(input('give height for diamond: '))
h = choice
r=1
v = h
change = False
if h % 2 == 0:
    h += 1
for i in range(h):
    print('  ' * v,'* ' * r)
    if change == True:
        v += 1
        r -= 2
    else:
        v -= 1
        r += 2
    if r >= h:
        change = True
    
choice = int(input('give height for A: '))
h = choice
r,n=0,2
v = h
change = False
for i in range(h):
    if i == (h//2):
        print(' ' * v + '*' + '*' * r + '*') 
    else:
        print(' ' * v + '*' + ' ' * r + '*')
    v -= 1
    r += 2
    