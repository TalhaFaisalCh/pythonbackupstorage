
from PokemonMoves import Move
class Pokemon_Type:
    def __init__(self, name, supereffective, notsupereffective, resist, weakness):
        self.name = name
        self.supereffective = supereffective
        self.notsupereffective = notsupereffective
        self.resist = resist
        self.weakness = weakness
    
    # def typing(self):
    #     self.normal = Pokemon_Type('normal', [], [], [], [])
    #     self.fire = Pokemon_Type('fire', ['grass'], ['water'], ['grass'], ['water'])
    #     self.water = Pokemon_Type('water', ['fire'], ['grass'], ['fire'], ['grass'])
    #     self.grass = Pokemon_Type('grass', ['water'], ['fire'], ['water'], ['fire'])
