from PokemonBattle import PokemonBattle 
from PokemonType import Pokemon_Type
from PokemonMoves import Move

class Pokemon:
    def __init__(self, name, MAXHP, HP, attack, defense, SPA, SPD, speed, type1, type2, moveset, movepool):
        self.name = name
        self.MAXHP = MAXHP
        self.HP = MAXHP
        self.attack = attack
        self.defense = defense
        self.SPA = SPA
        self.SPD = SPD
        self.speed = speed
        self.type1 = type1
        self.type2 = type2
        self.moveset = moveset



player_team = []
player_party = []
enemy_team = []
enemy_party = []
Box = []

NOtype = Pokemon_Type('???', [], [], [], [])
normal = Pokemon_Type('normal', [], [], [], [])
fire = Pokemon_Type('fire', ['grass'], ['water', 'fire'], ['grass', 'fire'], ['water'])
water = Pokemon_Type('water', ['fire'], ['grass','water'], ['fire', 'water'], ['grass'])
grass = Pokemon_Type('grass', ['water'], ['fire','grass','poison'], ['water', 'grass'], ['fire','poison'])
poison = Pokemon_Type('poison', ['grass'], ['poison'], ['grass', 'poison'], [])
rock = Pokemon_Type('rock', ['fire', 'flying'], ['ground'], ['fire', 'poison', 'normal', 'flying'], ['water', 'grass', 'ground'])
ground = Pokemon_Type('ground', ['fire', 'rock', 'poison'], ['grass', 'flying'], ['fire', 'rock'], ['water', 'grass'])
flying = Pokemon_Type('flying', ['grass'], ['rock'], ['ground', 'grass'], ['rock'])


flamethrower = Move('flamethrower', fire, 95, 100, 'special', 'burn')
surf = Move('surf', water, 95, 100, 'special', None)

Charizard = Pokemon('Charizard', 297, 297, 204, 192, 254, 206, 236,fire, flying, [flamethrower])
Regirock = Pokemon('Regirock', 301, 301, 236, 436, 136, 236, 136, rock, NOtype, [])
Blastoise = Pokemon('Blastoise', 290, 290, 202, 236, 206, 246, 196,water, NOtype, [surf])

player_team = [Charizard]
enemy_team = [Blastoise]

print(player_team[0].type2.supereffective)

a = PokemonBattle()
a.battle(player_team, enemy_team, 0, 0, None, None)


#if charmander.type1.name in squirtle.type1.supereffective:
 #   print('it was supereffective') 





