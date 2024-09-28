import random
Spaces = ['BELLEVILLE', 'LECOURBE', 'VAUGIRARD', 'COURELLES', 'AVENUE OF REPUBLIC', 'VILLETE', 'AVENUE OF NEUTRALITY', 'PARADISE', 'MOZART AVENUE', 'SAINT MICHEAL', 'PALACE PIGALE', 'MATIGNON', 'BOULYARD MALESHERES', 'HENRI-MARTIN', 'SURBURB', 'PLACE PURSE', 'FAYETTE', 'AVENUE BRETEUIL', 'AVENUE FOCH', 'BOULYARD NASTURIUMS', 'CHAMPALLY', 'STREET OF PEACE', 'CHANCE', 'CHANCE', 'CHANCE','CHEST','CHEST','CHEST','INCOME TAX','LUXURY TAX', 'NTPARNASSE', 'LYON', 'NORTH', 'SAINT LAZARE', 'ELECTRICAL WORKS', 'WATER WORKS', 'GTOJAIL', 'FREEPARKING']
SpaceText = ['land', 'land', 'land', 'land', 'land', 'land', 'land', 'land', 'land', 'land', 'land', 'land', 'land', 'land', 'land', 'land', 'land', 'land', 'land', 'land', 'land', 'land', 'Chance!', 'Chance!', 'Chance!', 'Community Chest!', 'Community Chest!', 'Community Chest!', 'Pay your income taxes!', 'Pay your luxury taxes!', 'land', 'land', 'land', 'land', 'land', 'land', 'GO TO JAIL!', 'Get 500PRK']
space_dict = dict(zip(Spaces, SpaceText))

while True:
    choice = int(input('which space?: ')) - 1
    choice = Spaces[choice]
    if space_dict[choice] == "land":
        option = input('Buy Y/N?: ')
        print(choice if option == 'Y' else "ok")