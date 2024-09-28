import random
from cyborg import Cyborg
from move import Move

class CyberMechanic:
    def __init__(self, name):
        self.name = name
        self.robot_list = []

    def createCyborg(self):
        ram = {'name' : 'ram', 'TYPE' : 'damage', 'power' : 4, 'accuracy' : 19, 'effect' : None}
        takedown = {'name' : 'takedown', 'TYPE' : 'damage', 'power' : 10, 'accuracy' : 16, 'effect' : None}
        axe = {'name' : 'axe', 'TYPE' : 'damage', 'power' : 9, 'accuracy' : 17, 'effect' : None}
        dagger = {'name' : 'dagger', 'TYPE' : 'damage', 'power' : 6, 'accuracy' : 20, 'effect' : None}
        chainsaw = {'name' : 'chainsaw', 'TYPE' : 'damage', 'power' : 15, 'accuracy' : 11, 'effect' : None}
        shuriken = {'name' : 'shuriken', 'TYPE' : 'damage', 'power' : 7, 'accuracy' : 18, 'effect' : None}
        flamethrower = {'name' : 'flamethrower', 'TYPE' : 'damage', 'power' : 8, 'accuracy' : 19, 'effect' : 'burn'}
        thunderbolt = {'name' : 'thunderbolt', 'TYPE' : 'damage', 'power' : 8, 'accuracy' : 19, 'effect' : 'PAR'}
        zapcannon = {'name' : 'zapcannon', 'TYPE' : 'damage', 'power' : 15, 'accuracy' : 10, 'effect' : 'PAR'}
        cut = {'name' : 'cut', 'TYPE' : 'damage', 'power' : 5, 'accuracy' : 19, 'effect' : None}
        drill = {'name' : 'drill', 'TYPE' : 'damage', 'power' : 9, 'accuracy' : 18, 'effect' : None}
        sonicboom = {'name' : 'sonicboom', 'TYPE' : 'damage', 'power' : 7, 'accuracy' : 20, 'effect' : None}
        crabhammer = {'name' : 'crabhammer', 'TYPE' : 'damage', 'power' : 11, 'accuracy' : 17, 'effect' : None}
        moonlight = {'name' : 'moonlight', 'TYPE' : 'recovery', 'power' : 5, 'accuracy' : 20, 'effect' : None}
        recover = {'name' : 'recover', 'TYPE' : 'recovery', 'power' : 7, 'accuracy' : 20, 'effect' : None}
        moves = [ram, axe, recover, moonlight, dagger, chainsaw, shuriken, flamethrower, cut, takedown, thunderbolt, zapcannon, drill, sonicboom, crabhammer] 
        
        # moves = [
        #             Move("dagger", "damage", 6, 20, None), 
        #             Move("axe", "damage", 6, 20, None)
        # ]
        # moves = {
        #             'ram': {'name': 'ram', 'TYPE': 'damage', 'power': 4, 'accuracy': 19, 'effect': None},
        #             'takedown': {'name': 'takedown', 'TYPE': 'damage', 'power': 10, 'accuracy': 16, 'effect': None},
        #             'axe': {'name': 'axe', 'TYPE': 'damage', 'power': 9, 'accuracy': 17, 'effect': None},
        #             'dagger': {'name': 'dagger', 'TYPE': 'damage', 'power': 6, 'accuracy': 20, 'effect': None},
        #             'chainsaw': {'name': 'chainsaw', 'TYPE': 'damage', 'power': 15, 'accuracy': 11, 'effect': None},
        #             'shuriken': {'name': 'shuriken', 'TYPE': 'damage', 'power': 7, 'accuracy': 18, 'effect': None},
        #             'flamethrower': {'name': 'flamethrower', 'TYPE': 'damage', 'power': 8, 'accuracy': 19, 'effect': 'burn'},
        #             'thunderbolt': {'name': 'thunderbolt', 'TYPE': 'damage', 'power': 8, 'accuracy': 19, 'effect': 'PAR'},
        #             'zapcannon': {'name': 'zapcannon', 'TYPE': 'damage', 'power': 15, 'accuracy': 10, 'effect': 'PAR'},
        #             'cut': {'name': 'cut', 'TYPE': 'damage', 'power': 5, 'accuracy': 19, 'effect': None},
        #             'drill': {'name': 'drill', 'TYPE': 'damage', 'power': 9, 'accuracy': 18, 'effect': None},
        #             'sonicboom': {'name': 'sonicboom', 'TYPE': 'damage', 'power': 7, 'accuracy': 20, 'effect': None},
        #             'crabhammer': {'name': 'crabhammer', 'TYPE': 'damage', 'power': 11, 'accuracy': 17, 'effect': None},
        #             'moonlight': {'name': 'moonlight', 'TYPE': 'recovery', 'power': 5, 'accuracy': 20, 'effect': None},
        #             'recover': {'name': 'recover', 'TYPE': 'recovery', 'power': 7, 'accuracy': 20, 'effect': None}
        #         }

        
        
        
        
        name = ['Battlebot', 'StealthX', 'ChatGPT', 'annihilator', 'DeathBox', 'Klawf', 'Radio123', 'Wheelz', 'Hjaro', 'QWERT', 'Typhoon', 'Tank', 'Legend518', 'AFB748', 'PikachuBOT', 'AcidArmour', 'Popcorn', 'Travis', 'Zinc', 'IronMoth', '502imcoming', 'CivicZero','Beldum','Caesar','Dominant','Australlia','Google','Slateport','Scope720','Nebula','Viper','Ferrari','VBA','NO$gba','DeSmuME','AlbertGrey','TurtleShell','Somehow9','SMFriedM','WalkingWake','IronLeaves','ThunderClap','Fluttermane','Chien-pao','Chi-yu','Miraidon','Deomorph','Neo']
        body = ['steel', 'aluminum', 'cobolt']
        enhancement = []
        while len(enhancement) != 4:
            i = moves[random.randint(0, len(moves) - 1)]
            if recover not in enhancement and i == recover:
                enhancement.append(i)
            elif i == recover:
                pass
            else:
                enhancement.append(i)
                
            

        c1 = Cyborg(name[random.randint(0, len(name) - 1)] , random.randint(90, 120), 100, enhancement, 10, None, body[random.randint(0, 2)])
        enhancement.clear
        self.robot_list.append(c1)


    def winPrediction(self, c, enemy_strength):
        if c.skill > enemy_strength:
            print('Victory for', c.name)
        else:
            print('Loss for', c.name)
