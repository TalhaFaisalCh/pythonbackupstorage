import random
import time
c1 = None
c2 = None


    







if __name__ == "__main__":

    alina = CyberMechanic()     
    alina.createCyborg()
    c1=alina.robot_list[0]
    alina.createCyborg()
    c2=alina.robot_list[1]
    t = Tournament()
    t.battle(c1, c2)


