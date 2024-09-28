import random
import time
# and List[rng_player] != rng_player_victim
def battle(attacker, defender, turn):
    while True:            
        turn += 1
        rng = random.randint(1, 5)
        if rng == 1:
            if turn % 2 == 0:
                print(attacker, 'strikes', defender + '!')
                time.sleep(0.5)
                rngb = random.randint(1, 5)
                if rngb == 1:
                    time.sleep(1)
                    print(defender, 'dies!')
                    return defender
                if rngb == 2:
                    time.sleep(1)
                    print(defender, 'got injured!')
                if rngb == 3:
                    print('The attack missed!')
            else:
                print(defender, 'strikes', attacker + '!')
                time.sleep(0.5)
                rngb = random.randint(1, 5)
                if rngb == 1:
                    time.sleep(1)
                    print(attacker, 'dies!')
                    return attacker
                if rngb == 2:
                    time.sleep(1)
                    print(attacker, 'got injured!')
                if rngb == 3:
                    print('The attack missed!')
        if rng == 2:
            if turn % 2 == 0:
                print(attacker, 'attempts to flee!')
                rngb = random.randint(0, 1)
                time.sleep(0.5)
                if rngb == 1:
                    print('they successfully fled!')
                    return 'draw'
                else:
                    print('but it failed!')
            else:
                print(defender, 'attempts to flee!')
                rngb = random.randint(0, 1)
                time.sleep(0.5)
                if rngb == 1:
                    print('they successfully fled!')
                    return 'draw'
                else:
                    print('but it failed!')

        if rng == 3:
            if turn % 2 == 0:
                print(attacker, 'kept a distance from', defender)
            else:
                print(defender, 'kept a distance from', attacker)

        else:
            print('.....')

        time.sleep(1)

List = []


print('welcome to hunger game emulator! This is where you can emulate a typical hunger game :O')
pack=int(input('how many player pack(each pack is 12 players): '))
player=12*pack

for i in range(player):
    print('what is the name of player' , i+1)
    choice = input('')
    List.append(choice)

Cornucopia_war = True
Cornucopia_war_list = []
flee_list = []
rng = 0
rngb = 0
minute = 0
day = True
night = False
while len(List) > 1:
    minute += 1
    rng_player = random.randint(0, len(List) - 1)
    rng_player_victim = random.randint(0, len(List) - 1)
    if Cornucopia_war == True and Cornucopia_war_list == []:
        for i in range(player):
            time.sleep(0.75)
            rng = random.randint(0,1)
            if rng == 0:
                print(List[i], 'fled.')
                flee_list.append(List[i])
            else:
                print(List[i], 'went to the Cornucopia!')
                Cornucopia_war_list.append(List[i])
        

    rng = random.randint(0, 3)
    if Cornucopia_war == True:
        rng = random.randint(0, 1)
    if rng == 0 and night == True:
        rng = random.randint(0, 3)
    if rng == 0 :
        if Cornucopia_war == True:
                rng_player = random.randint(0, len(Cornucopia_war_list) - 1)
                rng_player_victim = random.randint(0, len(Cornucopia_war_list) - 1)
                if Cornucopia_war_list[rng_player][0] != Cornucopia_war_list[rng_player_victim][0]:
                    print(Cornucopia_war_list[rng_player], 'battles', Cornucopia_war_list[rng_player_victim])
                    fight = battle(Cornucopia_war_list[rng_player], Cornucopia_war_list[rng_player_victim], -1)
                    if fight == 'draw':
                        pass
                    else:
                        List.remove(fight)
                        try:
                            Cornucopia_war_list.remove(fight)
                        except:
                            pass
        if rng_player != rng_player_victim and List[rng_player][0] != List[rng_player_victim][0]:
                
            
            print(List[rng_player], 'battles', List[rng_player_victim])
            time.sleep(1.25)
                
            fight = battle(List[rng_player], List[rng_player_victim], -1)
            if fight == 'draw':
                pass
            else:
                List.remove(fight)

    elif rng == 1 and day == True:
        if Cornucopia_war == True:
            try:
                print(flee_list[rng_player], 'picked up a backpack.')
                time.sleep(0.25)
                rngb = random.randint(1, 10)
                if rngb == 1:
                    print('but it was empty!')
            except:
                pass
        else:
            rngb = random.randint(0, 1)
            if rngb == 0:
                print(List[rng_player], 'found sticks.')
            elif rngb == 1:
                print(List[rng_player], 'found a potion.')
                rngb = random.randint(1, 16)
                if rngb == 1 and len(List) > 6:
                    time.sleep(1.5)
                    print('it turned out to be poison and they died')
                    List.remove(List[rng_player])
            elif rngb == 2:
                print(List[rng_player], 'got resources from their sponsers.')
            elif rngb == 3:
                print(List[rng_player], 'found berries.')
                rngb = random.randint(1, 10)
                if rngb == 1 and len(List) > 6:
                    print('they turned out poisonious.')
                    List.remove(List[rng_player])
    elif rng == 2 and day == True:
        rngb = random.randint(0, 1)
        if rngb == 0:
            rngb = random.randint(1, 6)
            if rngb == 1 and len(List) > 6:
                print(List[rng_player], 'tried to climb a tree but fell to their death.')
                List.remove(List[rng_player])
            else:
                print(List[rng_player], 'climbed a tree to gain ground.')
        
        elif rngb == 1:
            print(List[rng_player], 'is scouting out for resources.')

    elif rng == 3 and day == True:
        rngb == random.randint(0, 1)
        if rngb == 0:
            rngb == random.randint(1, 3)
            if rngb == 1:
                print(List[rng_player], 'hunted down a rabbit')
            if rngb == 2:
                print(List[rng_player], 'hunted down a goat')
            if rngb == 3:
                print(List[rng_player], 'hunted down a wolf')
        elif rngb == 1:
            print(List[rng_player], 'located a pool of water')
            rngb = random.randint(1, 10)
            if rngb == 1:
                print('turned out it was poisoned.')
                List.remove(List[rng_player])

    elif rng == 1 and night == True:
        rngb = random.randint(0, 2)
        if rngb == 0:
            print(List[rng_player], 'started a campfire.')
        elif rngb == 1:
            print(List[rng_player], 'failed to start a fire!')
            rngb = random.randint(1, 7)
            if rngb == 1:
                time.sleep(1)
                print('they froze to death!')
                List.remove(List[rng_player])
        elif rngb == 2:
            print(List[rng_player], 'used sticks as shelter.')
    
    elif rngb == 2 and night == True:
        print(List[rng_player], 'fell asleep')
        rngb = random.randint(0, 2)
        if rngb == 1 and List[rng_player][0] != List[rng_player_victim][0]:
            print(List[rng_player_victim], 'stole some resources from', List[rng_player])
            rngb = random.randint(1, 2)
            if rngb == 1:
                print(List[rng_player], 'woke up!')
                rngb = random.randint(1, 3)
                if rngb == 3:
                    print(List[rng_player], 'lost', List[rng_player_victim])
                else:
                    print(List[rng_player], 'battles', List[rng_player_victim])
                    fight = battle(List[rng_player], List[rng_player_victim], -1)
                    if fight == 'draw':
                        pass
                    else:
                        List.remove(fight)
    if minute > 20*pack:
        Cornucopia_war = False
    if minute % 10 == 0:
        print(List)
    if minute % 120 == 0:
        if day == True:
            night = True
            time.sleep(3)
            print('its now night time!')
            day = False
        else:
            day = True
            time.sleep(2)
            print('its now day time!')
            night = False
    time.sleep(1.5)
print(List[0], 'wins!')