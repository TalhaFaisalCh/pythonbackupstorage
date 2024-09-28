import time, random, threading
def input_with_timeout(prompt, timeout):
    print(prompt)
    user_input = [None]

    def input_thread():
        user_input[0] = input()
    
    thread = threading.Thread(target=input_thread)
    thread.start()
    thread.join(timeout)

    if thread.is_alive():
        thread.join()  # Wait for the thread to finish
        return None
    else:
        return user_input[0]
    

def battle(player_party, enemy_party):
    while True:    
        for i in range(len(player_party)):
            choice = int(input(f"What does {player_party[i].name} do?: attack[1], bag[2], run[3]: "))
            if choice == 1:
                    for m in range(len(player_party[i].moveset)):
                        print(player_party[i].moveset[m].name)
                    choice = int(input(''))
                    choice -= 1
                    move_select = player_party[i].moveset[choice]
                    if move_select.CAT in ('Attack'):
                        print('Target?')
                        for t in range(len(enemy_party)):
                            print(enemy_party[t].name)
                        target = int(input(''))
                        target -= 1
                        time.sleep(1)
                        print(player_party[i].name, 'used', str(move_select.name) + '!')


                        damage = player_party[i].attack + move_select.power - enemy_party[target].defense
                        if damage < 1:
                            damage = 1
                        enemy_party[target].HP -= damage
                        print(enemy_party[target].name + ':', str(enemy_party[target].HP) + '/' + str(enemy_party[target].MAXHP))
                        if enemy_party[target].HP <= 0:
                            print(enemy_party[target].name, 'fainted!')
                            enemy_party.remove(enemy_party[target])
                    else:
                        if move_select.CAT == 'status':
                            print('Target?')
                            for t in range(len(enemy_party)):
                                print(enemy_party[t].name)
                            target = int(input(''))
                            time.sleep(1)
                            print(player_party[i].name, 'used', str(move_select.name) + '!')
        
                            if move_select.effect == 'PAR':
                                print(enemy_party[target].name, 'is now paralysed!')
                                enemy_party[target].status = 'PAR'
                                if move_select.effect == 'psn':
                                    print(enemy_party[target].name, 'is now poisoned!')
                                    enemy_party[target].status = 'psn'
                    
        for i in range(len(enemy_party)):
            choice = 1
            if choice == 1:
                    choice = 1
                    choice -= 1
                    move_select = enemy_party[i].moveset[choice]
                    if move_select.CAT in ('Attack'):
                        target = 1
                        target -= 1
                        n = random.randint(2, 20)
                        n = n/10
                        Block = input_with_timeout("", n)
                        if Block is None:
                            print('')
                            print('')
                            print('')
                            print(enemy_party[i].name, 'used', str(move_select.name) + '!')
                            Block = input_with_timeout("Block!: ", enemy_party[i].timer)
                            if Block is not None:
                                print('Nice!')
                                damage = (enemy_party[i].attack + move_select.power)/2 - player_party[target].defense
                                damage = int(damage)
                            else:
                                damage = enemy_party[i].attack + move_select.power - player_party[target].defense
                        else:
                            damage = enemy_party[i].attack + move_select.power - player_party[target].defense
                        if damage < 1:
                            damage = 1
                        player_party[target].HP -= damage
                        print(player_party[target].name + ':', str(player_party[target].HP) + '/' + str(player_party[target].MAXHP))
                    else:
                        if move_select.CAT == 'status':
                            print('Target?')
                            for t in range(len(enemy_party)):
                                print(enemy_party[t].name)
                            target = int(input(''))
                            time.sleep(1)
                            print(player_party[i].name, 'used', str(move_select.name) + '!')
        
                            if move_select.effect == 'PAR':
                                print(enemy_party[t].name, 'is now paralysed!')
                                enemy_party[t].status = 'PAR'
                                if move_select.effect == 'psn':
                                    print(enemy_party[target].name, 'is now burnt!')
                                    enemy_party[target].status = 'psn'        
        if len(enemy_party) == 0:
            return 'victory'

