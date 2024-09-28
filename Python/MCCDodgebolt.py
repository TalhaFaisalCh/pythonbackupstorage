import random
import time
red = []
blue = []
def dodgebolt(red, blue):
    turn = 0
    turn += random.randint(1,2)
    rng = 0
    field = 0
    count=1
    while True:
        x = random.randint(2,10)
        for i in range(x):
            print('.....'*i)
            time.sleep(1.25)
        rngred = random.randint(0,len(red)-1)
        rngblue = random.randint(0,len(blue)-1)
        if turn % 2 == 0:        
            print(red[rngred], 'shot at', blue[rngblue])
        else:
            print(blue[rngblue], 'shot at', red[rngred])
        rng = random.randint(1, 10)
        time.sleep(0.66)
        if turn % 2 == 0:
            if rng > 6-field:
                print(blue[rngblue],'got eliminated!')
                blue.remove(blue[rngblue])
        else:
            if rng > 6-field:
                print(red[rngred],'got eliminated!')
                red.remove(red[rngred])
        count += 1
        time.sleep(0.2)
        if red == []:
            return "blue won!"
        elif blue == []:
            return "red won!"
        elif count == 2:
            turn += 1
            count = 0
        if turn % 6 == 0 and count == 0:
            field += 1
            print('The field got smaller!')

red = ["Charmander", "Squirtle", "Bulbasaur", "Pikachu"]
#blue = ["Cyndaquil", "Totodile", "Chikorita", "Phanpy"]
#blue = ["Chimchar", "Piplup", "Turtwig", "Riolu"]
#blue = ["Tepig", "Oshawott", "Snivy", "Zorua"]
#blue = ["Scorbunny", "Sobble", "Grookey", "Dreepy"]
blue = ["Fennikin", "Froakie", "Chespin", "Espurr"]
#blue = ["Torchic", "Mudkip", "Treeko", "Snorunt"]
#blue = ["Litten", "Popplio", "Rowlet", "Poipole"]
dodgebolt(red, blue)