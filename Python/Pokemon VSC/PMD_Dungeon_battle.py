import time, random
def battle(player_party, enemy_party):
    speed_check = 9999
    damage=0
    while True:    
        for i in range(len(player_party)):
            if player_party[i].speed == speed_check or player_party[i].speed // 10 == speed_check or player_party[i].speed // 100 == speed_check or player_party[i].speed // 1000 == speed_check:
                choice = int(input(f"What does {player_party[i].name} do?: attack[1], special[2], bag[3], run[4]: "))
                if choice == 1:
                    for m in range(len(player_party[i].moveset)):
                        print(player_party[i].moveset[m].name)
                    choice = int(input(''))
                    choice -= 1
                    move_select = player_party[i].moveset[choice]
                    accuracy = random.randint(0, 100)
                    if move_select.CAT in ('physical','special'):
                        print('Target?')
                        for t in range(len(enemy_party)):
                            print(enemy_party[t].name)
                        target = int(input(''))
                        target -= 1
                        time.sleep(1)
                        print(player_party[i].name, 'used', str(move_select.name) + '!')
                        if accuracy > move_select.accuracy:
                            print('The attack missed!')
                        else:
                            if move_select.CAT == 'physical':
                                damage = player_party[i].attack+move_select.power - (enemy_party[t].defense*2)
                            else:
                                damage = player_party[i].special+move_select.power - (enemy_party[t].special*2)
                        if damage < 1:
                            damage = 1
                        enemy_party[t].HP -= damage
                        print(enemy_party[t].name + ':', str(enemy_party[t].HP) + '/' + str(enemy_party[t].MAX_HP))
                    else:
                        if move_select.CAT == 'status':
                            print('Target?')
                            for t in range(len(enemy_party)):
                                print(enemy_party[t].name)
                            target = int(input(''))
                            time.sleep(1)
                            print(player_party[i].name, 'used', str(move_select.name) + '!')
                            if accuracy > move_select.accuracy:
                                print('The attack missed!')
                            else:
                                if move_select.effect == 'PAR':
                                    print(enemy_party[t].name, 'is now paralysed!')
                                    enemy_party[t].status = 'PAR'
                                if move_select.effect == 'Burn':
                                    print(enemy_party[t].name, 'is now burnt!')
                                    enemy_party[t].status = 'Burn'
                        if move_select.CAT == 'Debuff':
                            pass




        speed_check -= 1
        if speed_check < 1:
            speed_check = 9999
            return 'a'