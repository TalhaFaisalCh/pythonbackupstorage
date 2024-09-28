import random
import time
class Map:
    def __init__(self, x, y):
        self.x = x
        self.y = y
class Position:
    def __init__(self, x, y, found):
        self.x = x
        self.y = y
        self.found = found
CHEST = Position(1,0, False)
cat = Position(19,2,False)
tries = 75
class Player:
    def __init__(self, position):
        self.position = position
    def move(self, direction):
        if direction == 'w':
            self.y += 1
        elif direction == 's':
            self.y -= 1
        elif direction == 'a':
            self.x -= 1
        elif direction == 'd':
            self.x += 1
        elif direction == 'w1':
            self.y += 5
        elif direction == 's1':
            self.y -= 5
        elif direction == 'a1':
            self.x -= 5
        elif direction == 'd1':
            self.x += 5

player = Position(0, 0, True)
lowerX = 0
lowerY = 0
upperX = 0
upperY = 0
while tries > 1:
    print(player.x, player.y)
    choice = input('where to move?: ')
    Player.move(player, choice)
    lowerX = player.x
    upperX = player.x
    lowerY = player.y
    upperY = player.y
    count = 0
    for i in range(10):  
        if lowerX == cat.x:
            count += 1
            break
        lowerX -= 1
    for i in range(10):
        lowerY -= 1
        if lowerY == cat.y:
            count += 1
            break 

    for i in range(10):
        if upperX == cat.x:
            count += 1
            break
        upperX += 1
    for i in range(10):
        if upperY == cat.y:
            count += 1
            break
        upperY += 1
    
    if count > 1:
        print('something is nearby')