from cybermechanic import CyberMechanic
from tournament import Tournament

if __name__ == "__main__":
    t = Tournament()
    alina = CyberMechanic('alina')
    for i in range(8192):
        alina.createCyborg()
    round = -1
    group = 0
    while len(alina.robot_list) != 8:
        round += 1
        if round + 2 > len(alina.robot_list):
            round = 0
        c1=alina.robot_list[round]
        c2=alina.robot_list[round + 1]
        
        winner = t.Tbattle(c1, c2)
        if winner == 1:
            alina.robot_list.remove(c2)
        if winner == 2:
            alina.robot_list.remove(c1)
        
    while len(alina.robot_list) != 1:
        round += 1
        if round + 2 > len(alina.robot_list):
            round = 0
        c1=alina.robot_list[round]
        c2=alina.robot_list[round + 1]
        
        winner = t.battle(c1, c2)
        if winner == 1:
            alina.robot_list.remove(c2)
        if winner == 2:
            alina.robot_list.remove(c1)
                                                