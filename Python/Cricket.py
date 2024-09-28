import time
import random
class Player:
    def __init__(self, name, bat_skill, speed, handed, proffesion):
        self.name = name
        self.bat_skill = bat_skill
        self.speed = speed
        self.handed = handed
        self.proffesion = proffesion

Babar = Player('Babar', 92, 80, 'right', 'batsman')
Rizwan = Player('Rizwan', 90, 78, 'right', 'keeper')
Fakhar = Player('Fakhar', 85, 80, 'left', 'batsman')



pakistan_team = [Babar, Rizwan, Fakhar]


test1 = Player('Eric', 51, 80, 'right', 'batsman')
test2 = Player('Ludo', 50, 80, 'right', 'batsman')
test3 = Player('Roll', 70, 80, 'right', 'batsman')

test_team = [test1, test2, test3]


class match:
    def match(team1, team2):
        rng = random.randint(1, 2)
        if rng == 1:
            print(team2 ,'bats first!')
            setter = 2
        if rng == 2:
            print(team1, 'bats first!')
            setter = 1
        
        over = 0
        setter=1
        if setter == 1:
            bat_posistion = []
            map(lambda i:bat_posistion.append(i))
            
            while over != 20:
                choice1 = int(input('What play?: safe[1], average[2], risky[3]'))
                choice2 = int(input('What inning?: inward[1], average[2], outward[3]'))

                ball_inning=random.randint(1, 3)

                rng = random.randint(1, 100)
                


    