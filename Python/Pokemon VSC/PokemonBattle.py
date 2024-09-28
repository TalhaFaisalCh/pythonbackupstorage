import time
import random
class PokemonBattle:
    def battle(self, player_team, enemy_team, Pparty, Eparty, pa1, ea1):
        pa1 = player_team[0]
        print('Player sent out', pa1.name)
        ea1 = enemy_team[0]
        print('Opponent sent out', ea1.name)
        player_switch = player_team
        enemy_switch = enemy_team
        Pparty = len(player_team)
        Eparty = len(enemy_team)
        while Pparty != 0 and Eparty != 0:
            print('What will', pa1.name, 'do?')
            for i in range(len(pa1.moveset)):
                print(pa1.moveset[i].name)
            confirm = False
            while confirm == False:
                choice=int(input('Pick a move[1-4], switch[0]: '))
                choice -= 1
                if choice == -1:
                    if Pparty == 1:
                        print('There is no mon to switch into!')
                    else:
                        print('Who do you want to switch into [1-5]:')
                        for i in range(len(player_switch)):
                            print(player_team[i].name)
                        choice=int(input(''))
                        choice -= 1
                        pa1 = player_team[choice]
                        Pselection = ''
                        confirm = True
                else:
                    Pselection = pa1.moveset[choice]
                    print(Pselection.name)
                    print(Pselection.power)
                    confirm = True
            choice=-2
            confirm = False
            while confirm == False:
                for i in range(len(ea1.moveset)):
                    if (pa1.type1 in ea1.moveset[i].type.supereffective or pa1.type2 in ea1.moveset[i].type.supereffective) and \
                     (pa1.type1 not in ea1.moveset[i].type.notsupereffective or pa1.type2 in ea1.moveset[i].type.notsupereffective):
                        choice=i
                if choice == -2:
                    choice = random.randint(0,len(ea1.moveset) - 1)
                Eselection = ea1.moveset[choice]
                confirm = True

                switch_ai = 4
                if (ea1.type1 in pa1.type1.supereffective or ea1.type1 in pa1.type2.supereffective or ea1.type2 in pa1.type1.supereffective or ea1.type2 in pa1.type2.supereffective) and \
                (ea1.type1 not in pa1.type1.notsupereffective or ea1.type1 not in pa1.type2.notsupereffective or ea1.type2 not in pa1.type1.notsupereffective or ea1.type2 not in pa1.type2.notsupereffective) and \
                switch_ai == 4:
                    for i in range(enemy_switch):
                        if(enemy_team[i].type1 in pa1.type1.supereffective or enemy_team[i].type1 in pa1.type2.supereffective or enemy_team[i].type2 in pa1.type1.supereffective or enemy_team[i].type2 in pa1.type2.supereffective) and \
                        (enemy_team[i].type1 not in pa1.type1.notsupereffective or enemy_team[i].type1 not in pa1.type2.notsupereffective or enemy_team[i].type2 not in pa1.type1.notsupereffective or enemy_team[i].type2 not in pa1.type2.notsupereffective):
                            switch_ai = i
                    ea1 = enemy_team[switch_ai]
                    Eselection = ''

            game_speed = 255
            x=1

            while game_speed > -50:
                x=1
                
                if pa1.speed == game_speed and pa1.HP > 0 and Pselection != '':
                    print(pa1.name, 'used', Pselection.name)
                    accuracy = random.randint(1, 20)
                    if accuracy > Pselection.accuracy:
                        print('The attack missed')
                    else:
                        
                        if pa1.type1 == Pselection.type or pa1.type2 == Pselection.type:
                            x = 1.5
                        ea1.HP -= pa1.attack + (Pselection.power * x)
                        ea1.HP = int(ea1.HP)
                        print(ea1.name + ':', str(ea1.HP) + '/' + str(ea1.MAXHP))
                    time.sleep(0.5)
                
                if ea1.speed == game_speed and ea1.HP > 0 and Eselection != '':
                    print(ea1.name, 'used', Eselection.name)
                    accuracy = random.randint(1, 20)
                    if accuracy > Eselection.accuracy:
                        print('The attack missed')
                    else:
                        
                        if ea1.type1 == Eselection.type or ea1.type2 == Eselection.type:
                            x = 1.5
                        pa1.HP -= ea1.attack + (Eselection.power * x)
                        pa1.HP = int(pa1.HP)
                        print(pa1.name + ':', str(pa1.HP) + '/' + str(pa1.MAXHP))
                    time.sleep(0.5)
                if pa1.HP < 1:
                    print(pa1.name, 'fainted!')
                    player_switch.remove(pa1)
                    Pparty -= 1
                    time.sleep(0.5)
                    if Pparty == 0:
                        print('You lost!')
                        break
                    else:
                        print('Who do you want to bring out next?')
                        for i in range(len(player_switch)):
                            print(player_team[i].name)
                        choice=int(input(''))
                        choice -= 1
                        pa1 = player_team[choice]
                        print(pa1.name, 'was sent!')
                        time.sleep(0.5)
                        Pselection = ''

                if ea1.HP < 1:
                    print(ea1.name, 'fainted!')
                    enemy_switch.remove(ea1)
                    Eparty -= 1
                    time.sleep(0.5)
                    if Eparty == 0:
                        print('You won!')
                        break
                    else:
                        switch_ai = -5
                        for i in range(len(enemy_switch)):
                            if(enemy_team[i].type1 in pa1.type1.supereffective or enemy_team[i].type1 in pa1.type2.supereffective or enemy_team[i].type2 in pa1.type1.supereffective or enemy_team[i].type2 in pa1.type2.supereffective) and \
                            (enemy_team[i].type1 not in pa1.type1.notsupereffective or enemy_team[i].type1 not in pa1.type2.notsupereffective or enemy_team[i].type2 not in pa1.type1.notsupereffective or enemy_team[i].type2 not in pa1.type2.notsupereffective):
                                switch_ai = i
                        if switch_ai == -5:
                            switch_ai = random.randint(0, len(enemy_switch)-1)
                        ea1 = enemy_team[switch_ai]
                        print(ea1.name, 'was sent!')
                        time.sleep(0.5)
                        Eselection = ''
                

                game_speed = game_speed - 1

                    


        
        
        

        