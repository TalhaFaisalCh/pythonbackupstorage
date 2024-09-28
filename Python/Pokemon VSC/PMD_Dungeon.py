from PokemonMoves import Move
from PMD_Dungeon_battle import battle
class character:
    def __init__(self,name, MAX_HP,HP,attack,defense,special, speed, level, xp, moveset, status, buff):
        self.name = name
        self.MAX_HP = MAX_HP
        self.HP = MAX_HP
        self.attack = attack
        self.defense = defense
        self.special = special
        self.speed = speed
        self.level = level
        self.xp = xp
        self.moveset = moveset
        self.status = None
        self.buff = None
    def levelup(self):
        self.MAX_HP += 5
        self.HP += 5
        self.attack += 3
        self.defense += 2
        self.special += 3
        self.speed += 4
Thunderbolt = Move('Thunderbolt', None, 8, 100, 'special', 'PAR')
Quickattack = Move('Quickattack', None, 4, 100, 'physical', None)
Thunderwave = Move('Thunderwave', None, 0, 80, 'status', 'PAR')
Agility = Move('Agility', None, 0, 100, 'buff-S', 'speed')
Wingattack = Move('Wingattack', None, 50, 100, 'physical', None)
Growl = Move('Growl', None, 0, 100, 'debuff-A', 'attack')

Pikachu = character('Pikachu', 50, 50, 40, 30, 40, 52, 5, 0, [Thunderbolt, Quickattack, Thunderwave, Agility], None, None)

Starly = character('Starly', 40, 40, 50, 20, 20, 45, 4, 50, [Wingattack, Quickattack, Growl], None, None)
player_party = []
enemy_party = []
player_party.append(Pikachu)
e1 = Starly
enemy_party.append(e1)
bag = []
battle(player_party, enemy_party)
print(Starly.HP)