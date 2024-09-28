import random
import time
c1 = None
c2 = None

class Cyborg:
    def __init__(self, name, MAX_HP, HP, enhancement, skill):
        self.name = name
        self.MAX_HP = 100
        self.HP = 100
        self.enhancement = enhancement
        self.skill = skill

    def trainForBattle(self):
        time.sleep(0.25)
        self.skill += 10
    
class CyberMechanic:
    def __init__(self, name):
        self.name = name
        self.robot_list = []

    def createCyborg(self):
        ram = {'name' : 'ram', 'TYPE' : 'damage', 'power' : 3, 'accuracy' : 19}
        axe = {'name' : 'axe', 'TYPE' : 'damage', 'power' : 7, 'accuracy' : 17}
        dagger = {'name' : 'dagger', 'TYPE' : 'damage', 'power' : 4, 'accuracy' : 20}
        recover = {'name' : 'recover', 'TYPE' : 'recovery', 'power' : 5, 'accuracy' : 20}
        moves = [ram, axe, recover, recover, dagger] 
        name = ['Battlebot', 'StealthX', 'ChatGPT', 'annihilator', 'DeathBox', 'Klawf', 'Radio123', 'Wheelz']

        enhancement = []
        for i in range(4):
            enhancement.append(moves[random.randint(0, len(moves) - 1)])

        c1 = Cyborg(name[random.randint(0, len(name) - 1)] , 100, 100, enhancement, 10)
        enhancement.clear
        self.robot_list.append(c1)


    def winPrediction(self, c, enemy_strength):
        if c.skill > enemy_strength:
            print('Victory for', c.name)
        else:
            print('Loss for', c.name)


class Tournament:
    def battle(self,c1,c2):
        print(c1.name)
        print(c1.enhancement)
        print(c2.name)
        print(c2.enhancement)
        time.sleep(15)
        while c1.HP > 0 and c2.HP > 0:
            selection = c1.enhancement[random.randint(0, 3)]
            accuracy = random.randint(1, 20)
            print(c1.name,'used', selection['name'])

            time.sleep(1)

            if selection['TYPE'] == 'recovery':              
                if c1.HP >= c1.MAX_HP:
                    print('But it failed!')
                else:
                    c1.HP += selection['power']
                    if c1.HP > c1.MAX_HP:
                        c1.HP = c1.MAX_HP

            elif accuracy > selection['accuracy']:
                print('The attack missed!')
            elif selection['TYPE'] == 'damage':
                critical = random.random(1, 12)
                if critical == 12:
                    c2.HP -= selection['power']
                    print('A critical hit!')
                    time.sleep(0.5)
                c2.HP -= selection['power']
                print(c2.name +':', str(c2.HP) + '/' + str(c2.MAX_HP))
            
            time.sleep(1)
            
            selection = c2.enhancement[random.randint(0, 3)]
            accuracy = random.randint(1, 20)
            print(c2.name,'used', selection['name'])

            time.sleep(1)

            if selection['TYPE'] == 'recovery':
                if c2.HP >= c2.MAX_HP:
                    print('But it failed!')
                else:
                    c2.HP += selection['power']
                    if c2.HP > c2.MAX_HP:
                        c2.HP = c2.MAX_HP

            elif accuracy > selection['accuracy']:
                print('The attack missed!')
            elif selection['TYPE'] == 'damage':
                critical = random.random(1, 12)
                if critical == 12:
                    c2.HP -= selection['power']
                    print('A critical hit!')
                    time.sleep(0.5)
                c1.HP -= selection['power']
                print(c1.name +':', str(c1.HP )+ '/' + str(c1.MAX_HP))
            
            time.sleep(1)







alina = CyberMechanic()     
alina.createCyborg()
c1=alina.robot_list[0]
alina.createCyborg()
c2=alina.robot_list[1]
t = Tournament()
t.battle(c1, c2)


