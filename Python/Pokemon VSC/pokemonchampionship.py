import time, random

def ACErace():
    print('GO!')
    for i in range(80):
        for i in range(3):
            time.sleep(0.5)
            print('...')
            time.sleep(0.5)
    




PlayerList = []
for i in range(40):
    print('player', i+1)
    choice = input('')
    PlayerList.append(choice)






random.shuffle(PlayerList)
red = []
blue = []
green = []
yellow = []
aqua = []
purple = []
black = []
cyan = []
orange = []
pink = []
for i in range(40):
    if i <= 3:
        red.append('RED-' + PlayerList[i])
    elif i <= 7:
        blue.append('BLUE-' + PlayerList[i])
    elif i <= 11:
        green.append('GREEN-' + PlayerList[i])
    elif i <= 15:
        yellow.append('YELLOW-' + PlayerList[i])
    elif i <= 19:
        aqua.append('AQUA-' + PlayerList[i])
    elif i <= 23:
        purple.append('PURPLE-' + PlayerList[i])
    elif i <= 27:
        black.append('BLACK-' + PlayerList[i])
    elif i <= 31:
        cyan.append('CYAN-' + PlayerList[i])
    elif i <= 35:
        orange.append('ORANGE-' + PlayerList[i])
    elif i <= 39:
        pink.append('PINK-' + PlayerList[i])

print(red)