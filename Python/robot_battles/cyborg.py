import time
class Cyborg:
    def __init__(self, name, MAX_HP, HP, enhancement, skill, status, body):
        self.name = name
        self.MAX_HP = MAX_HP
        self.HP = MAX_HP
        self.enhancement = enhancement
        self.skill = skill
        self.status = status
        self.body = body

    def trainForBattle(self):
        time.sleep(0.25)
        self.skill += 10