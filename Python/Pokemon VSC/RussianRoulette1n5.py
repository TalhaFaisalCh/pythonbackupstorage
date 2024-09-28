import time
import random
gun = ['live', 'live', 'live', 'blank', 'blank', 'blank', 'blank', 'blank']

random.shuffle(gun)

player_life = 5
dealer_life = 5
count = 0
player_item = []
dealer_item = []
def battle(count, player_life, dealer_life):
    choice = ''
    while (player_life and dealer_life) > 0:
        count += 1
        if count % 2 != 0:
            choice = ''
            while choice != 1:
                choice = int(input('what do you want to do?: shoot[1], item[2]'))
                if choice == 1:
                    choice = int(input('shoot: Dealer[1], Yourself[2]'))
                    if gun[0] == 'live' and choice == 1:
                        dealer_life -= 1
                        print(dealer_life , '/', 5)
                    elif gun[0] == 'live' and choice == 2:
                        player_life -= 1
                        print(player_life , '/', 5)
                    else:
                        print('blank shot')
                    gun.remove(gun[0])
                else:
                    print(player_item)
                    choice = int(input('use an item via index: '))
                    try:
                        if player_item[choice] == 'magnifying_glass':
                            print('You looked into the gun and it is a', gun[0], 'shot')
                            choice = 0
                    except:
                        pass

battle(count, player_life, dealer_life)
            
