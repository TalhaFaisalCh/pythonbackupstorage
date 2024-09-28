import random
import time
items = ['spider_eye', 'dragon_hide', 'dragon_heart', 'dragon_fang', 'newt_eye', 'dragon_fruit'
                , 'chocolate_frog','stardust','unicorn_horn','bat_wings','bat_fang','bat_venom','bone_powder']

dungeon = []
rng = 0
rooms = ['empty', 'item', 'trap']


print('Hello Wizard!')
time.sleep(1)
print("You are going to embark a 'legendary' quest on being the best potion master the world has ever seen!")
time.sleep(3)
class Potion:
    def __init__(self, name, description, power, time):
        self.name = name
        self.description = description
        self.power = power
        self.time = time

class Wizard:
    def __init__(self, name, capacity, quest_completion):
        self.name = name
        self.capacity = capacity
        self.quest_completion = quest_completion
    
    def brew_potion(self):
        if self.capacity > 0:
            self.capacity -= 1
            print('Potion has been created')
        else:
            print('All the bottles has been created!')

    
def complete_quest(self):
    dungeonIN = True
    time.sleep(0.5)
    print('Quest it is!')
    time.sleep(1)
    for i in range(20):
        rng = random.randint(1, 10)
        if rng <= 3:
            dungeon.append(rooms[0])
        elif rng <= 8 and rng > 3:
            dungeon.append(rooms[1])
        else:
            dungeon.append(rooms[2])
    
    time.sleep(1)

    print('Start!')
    print('NOTE: enter zero to leave')
    while dungeonIN == True:
        print('Where to go from 1 to', len(dungeon))
        choice = int(input('>>>'))
        choice -= 1
        time.sleep(1)

        if choice == -1:
            print('You had successfully left the dungeon')
            dungeonIN = False
        elif choice >= len(dungeon):
            print('Imagine trying to find the number that does not exist LOL.')
            time.sleep(0.5)
        elif dungeon[choice] == 'empty':
            print('It is an empty room.')
            time.sleep(1.5)
            dungeon.pop(choice)
        elif dungeon[choice] == 'item':
            print('You found a', items[random.randint(0, len(items) - 1)], '!')
            time.sleep(1.5)
            dungeon.pop(choice)
        elif dungeon[choice] == 'trap':
            print('A trap!')
            rng = random.randint(1, 5)
            time.sleep(2)
            if rng == 1:
                print('You lost!')
                dungeonIN = False
            else:
                print("You've escaped the trap!")
            time.sleep(1.5)
            dungeon.pop(choice)
        else:
            print('Imagine trying to find the number that does not exist LOL.')
            time.sleep(0.5)
    
    if len(dungeon) == 0:
        print('You have succesfully gone through the entire dungeon')
        dungeonIN = False
        self.quest_completion += 1

w1 = Wizard('Harry', 10, 0)
while True:
    choice = int(input('What are you going to do: quest[1], craft[2]: '))
    if choice == 1:
        w1.complete_quest()
    if choice == 2:
        w1.brew_potion()





