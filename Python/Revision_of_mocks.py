import random
import time
import math

DEF_list = ['Paralex error', 'Least Count(L.C)', 'Metre Ruler', 'Flexible measuring tape', 'Steel measuring tape', 'Vernier Calliper', 'Matter', 'Subatomic particles', 'Nucleon', 'Electronic Configuration(E.C)', 'Shells/Orbits', 'Valence Shell', 'Valence', 'Oxidation state', 'IONS']

elements = ["Hydrogen","Helium","Lithium","Beryllium","Boron","Carbon","Nitrogen","Oxygen","Fluorine","Neon","Sodium",
            "Magnesium","Aluminium","Silicon","Phosphorous","Sulfur","Chlorine","Argon","Potassium","Calcium"]
symbol = ["H","He","Li","Be","B","C","N","O","F","Ne","Na","Mg","Al","Si","P","S","Cl","Ar","K","Ca"]
proton = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
nucleon_number = [1, 4, 7, 9, 11, 12, 14, 16, 19, 20, 23, 24, 27, 28, 31, 32, 35, 40, 39, 40]
Group = ["n/a", "VIII", "I","II","III","IV","V","VI","VII","VIII","I","II","III","IV","V","VI","VII","VIII","I","II"]


x = 0
y = 0

Q = 0
I = 0


tries = 5

point = 0
Testmark = 0

option = ''

Type = int(input("What type of practice?: Math[1], Phy/chem[2], ALL OF THEM[3]"))


while tries != 0:
    Q = random.randint(5, 6)

    if Q == 1:
        Q = random.randint(1, 4)
        x = random.randint(16, 99)
        y = x*x
        if Q == 1:
            print("Find the square of", x)
            I = int(input(": "))
            time.sleep(0.5)
            if I == y:
                print("Correct!")
                point += 1
            else:
                print("Wrong!")
                time.sleep(0.75)
                print("The answer was", y)
        else:
            print("Find the square root of", y)
            I = int(input(": "))
            time.sleep(0.5)
            if I == x:
                print("Correct!")
                point += 1
            else:
                print("Wrong!")
                time.sleep(0.75)
                print("The answer was", x)
        Testmark += 1

    elif Q == 5:
        print('DEFINE:')
        for i in range(3):
            Q = random.randint(0 , len(DEF_list) - 1)
            print(DEF_list[Q])
            option = input('Got it correct?[Y/N]: ').lower()
            if option == 'y':
                print('Correct!')
                point += 1
            Testmark += 1
    
    elif Q == 6:
        choice = random.randint(0, len(elements) - 1)
        print("What is the symbol of", elements[choice], "?:")
        answer = str(input(""))
        if answer == symbol[choice]:
            print("Correct!")
            time.sleep(0.025)
            point += 1
        

        else:
            print("Wrong!")
            time.sleep(0.025)
            print("The symbol of", elements[choice], "was", symbol[choice])
            time.sleep(0.025)
        
        print("What is the proton number of", elements[choice], "?:")
        answer = int(input(""))
        if answer == proton[choice]:
            print("Correct!")
            time.sleep(0.025)
            point += 1
            
        else:
            print("Wrong!")
            time.sleep(0.025)
            print("The protonnumber of", elements[choice], "was", proton[choice])
            time.sleep(0.025)

        
        print("What is the nucleon number of", elements[choice], "?:")
        try:
            answer = int(input(""))
        except:
            answer = float(input(""))

        if answer == nucleon_number[choice]:
            print("Correct!")
            time.sleep(0.025)
            point += 1
            
        else:
            print("Wrong!")
            time.sleep(0.025)
            print("The nucleon nnumber of", elements[choice], "was", nucleon_number[choice])
            time.sleep(0.025)
        
        
        print("What is the Group number of", elements[choice], "?:")
        try:
            answer = str(input(""))
        except:
            answer = float(input(""))

        if answer == Group[choice]:
            print("Correct!")
            time.sleep(0.025)
            point += 1
            
        else:
            print("Wrong!")
            time.sleep(0.025)
            print("The Group nnumber of", elements[choice], "was", Group[choice])
            time.sleep(0.025)
        
        Testmark += 4






    tries -= 1


print("Your score:", point)
