import random, time
cation = {'Lithium': ['Li', 1, 'single'], 'Sodium': ['Na', 1, 'single'], 'Potassium': ['K', 1, 'single'], 'Rubidium': ['Rb', 1, 'single'], 'Caesium': ['Cs', 1, 'single'], 'Francium': ['Fr', 1, 'single'], 'Beryllium': ['Be', 2, 'single'], 'Magnesium': ['Mg', 2, 'single'], 'Calcium': ['Ca', 2, 'single'], 'Stronium': ['Sr', 2, 'single'], 'Barium': ['Ba', 2, 'single'], 'Radium': ['Ra', 2, 'single'], 'Boronium': ['B', 3, 'single'], 'Aluminium': ['Al', 3, 'single'], 'Indium': ['In', 3, 'single'], 'Zinc': ['Zn', 2, 'single'], 'Iron(II)': ['Fe', 2, 'single'], 'Iron(III)': ['Fe', 3, 'single'], 'Copper(I)': ['Cu', 1, 'single'], 'Copper(II)': ['Cu', 2, 'single'], 'Silver': ['Ag', 1, 'single'], 'Mercury': ['Hg', 1, 'single'], 'Gold': ['Au', 1, 'single'], 'Lead': ['Pb', 2, 'single'], 'Cobolt': ['Co', 2, 'single'], 'Tin': ['Sn', 2, 'single'], 'Ammonium': ['NH4', 1, 'multi'], 'Chromium' : ['Cr', 3, 'single']}
anion = {'Fluoride': ['F', 1, 'single'], 'Chloride': ['Cl', 1, 'single'], 'Bromide': ['Br', 1, 'single'], 'Iodide': ['I', 1, 'single'], 'Astatide': ['At', 1, 'single'], 'Oxygen': ['O', 2, 'single'], 'Sulfide': ['S', 2, 'single'], 'Selenide': ['Se', 2, 'single'], 'Nitride': ['N', 3, 'single'], 'Phosphide': ['P', 3, 'single'], 'Hydride': ['H', 1, 'single'], 'Hydroxide': ['OH', 1, 'multi'], 'Carbonate': ['CO3', 2, 'multi'], 'Hydrogen Carbonate': ['HCO3', 1, 'multi'], 'Nitrate': ['NO3', 1, 'multi'], 'Nitrite': ['NO2', 1, 'multi'], 'Sulfate': ['SO4', 2, 'multi'], 'Sulfite': ['SO3', 2, 'multi'], 'Phosphate': ['PO4', 3, 'multi'], 'Phosphite': ['PO3', 3, 'multi'], 'Manganate': ['MnO4', 1, 'multi'], 'Dichromate': ['Cr2O7', 2, 'multi'], 'Chlorate': ['ClO3', 1, 'multi']}
def combine(cations, anions):
    if cations[1] == anions[1]:
        return str(cations[0] + anions[0])
    elif cations[1] == 1:
        if anions[1] != 1:
            if cations[2] == 'multi':
                return str('(' + cations[0] + ')' + str(anions[1]) + anions[0])
            else:
                return str(cations[0] + str(anions[1]) + anions[0])
        else:
            str(cations[0] + anions[0])
    elif anions[1] == 1:
        if cations[1] != 1:
            if anions[2] == 'multi':
                return str(cations[0] + '(' + anions[0] + ')' + str(cations[1]))
            else:
                return str(cations[0] + anions[0] + str(cations[1]))
        else:
            str(cations[0] + anions[0])
    else:
        if cations[2] == 'multi' and anions[2] == 'multi':
            return str('(' + cations[0] + ')' + str(anions[1]) + '(' + anions[0] + ')' + str(cations[1]))
        elif cations[2] == 'multi':
            return str('(' + cations[0] + ')' + str(anions[1]) + anions[0] + str(cations[1]))
        elif anions[2] == 'multi':
            return str(cations[0] + str(anions[1]) + '(' + anions[0] + ')' + str(cations[1]))
        else:
            return str(cations[0] + str(anions[1]) + anions[0] + str(cations[1]))
point, Qs = 0, 0
while Qs < 30:
    n = random.randint(0, 27)
    Cationname = list(cation.keys())[n]
    Cationselect = list(cation.values())[n]
    n = random.randint(0, 22)
    Anionname = list(anion.keys())[n]
    Anionselect = list(anion.values())[n]
    print(Cationname, Anionname)
    time.sleep(1)
    answer = combine(Cationselect, Anionselect)
    choice = input('')
    if choice == answer:
        print('Correct!')
        point += 1
    else:
        print('Wrong!')
        time.sleep(0.25)
        print(answer)
    time.sleep(1.25)
    Qs += 1
print(point, '/', Qs)