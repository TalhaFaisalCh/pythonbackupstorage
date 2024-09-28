import threading
import time
from Eeveelution_dungeon_BATTLE import battle
def input_with_timeout(prompt, timeout):
    print(prompt)
    user_input = [None]

    def input_thread():
        user_input[0] = input()
    
    thread = threading.Thread(target=input_thread)
    thread.start()
    thread.join(timeout)

    if thread.is_alive():
        thread.join()  # Wait for the thread to finish
        return None
    else:
        print("Blocked!")
        return user_input[0]

# # Example usage:
# response = input_with_timeout("Dodge!: ", 0.75)  # Timeout set to 5 seconds
# if response is not None:
#     print("You entered:", response)


class Pokemon:
    def __init__(self, name, MAXHP, HP, attack, defense, resist, weakness, status, moveset, timer):
        self.name = name
        self.MAXHP = MAXHP
        self.HP = MAXHP
        self.attack = attack
        self.defense = defense
        self.resist = resist
        self.weakness = weakness
        self.status = status
        self.moveset = moveset
        self.timer = timer
class move:
    def __init__(self, name, power, type, CAT):
        self.name = name
        self.power = power
        self.type = type
        self.CAT = CAT

Tackle = move('Tackle', 3, 'normal', 'Attack')
Headbutt=move('Headbutt', 5, 'normal', 'Attack')


Eevee = Pokemon('Eevee', 30, 30, 1, 0, None, None, None, [Tackle], 1)
Zigzagoon = Pokemon('Zigzagoon', 9, 9, 0, 0, None, None, None, [Tackle], 0.66)
Poochyena = Pokemon('Poochyena', 8, 8, 1, 0, None, None, None, [Tackle], 0.75)
bag = ['potion', 'superpotion']
Jirachi = Pokemon('Jirachi', 80, 80, 3, 5, None, None, 'sleep', [], 0.2)

player_party = [Eevee]
enemy_party = [Zigzagoon, Poochyena]

battle(player_party, enemy_party)


