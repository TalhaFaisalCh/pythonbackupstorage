import random

roaming_list = ['Entei', 'Raikou', 'Latios', 'Moltres', 'Articuno', 'Umbreon', 'Mew', 'Manaphy', 'Heatran', 'Shaymin', 'Virizion', 'Thundurus']
location = ['NUST VILLA 11', 'park NUST', 'Beaconhouse', 'Shangrila apartment', 'apartment 5?', 'Texila', 'Guhgur', 'Centorous', 'Metro', 'Sir imran academy', 'THAT house within gughar', 'Airport', 'Gigamall', 'Oman?', 'Karachi?', 'Dina', 'Clothes_shop', 'OPTP', 'Bookshop', 'Toystore', 'Hiking']

for i in range(len(roaming_list)):
    print(roaming_list[i], 'is in location: ', location[random.randint(0, len(location) - 1)])
    