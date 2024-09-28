import random
from FunctionsONLYasModules import read_file

class Ruler():
    def __init__(self, name, confidence, nature, height):
        self.name = name
        self.confidence = confidence
        self.nature = nature
        self.height = height

class Heir(Ruler):
    def __init__(self, name, confidence, nature, height, heirscore):
        super().__init__(name, confidence, nature, height)
        self.heirscore = heirscore


#wordlist = read_file('')


Throne = Ruler('name', random.randint(1, 100), 'serious', random.randint(60, 84))





import time
heirlist = []
while True:
    for i in range(2, 6):
        heir = Ruler('name', random.randint(1, 100), 'serious', random.randint(60, 84))
        heir = Heir('name', random.randint(1, 100), 'serious', random.randint(60, 84), heir.confidence + heir.height)
        heirlist.append(heir)
    time.sleep(1)
    print('The heir is being chosen?')
    print(heirlist)
    time.sleep(1)
    print('The heir is:')
    time.sleep(0.5)
    largest = heirlist(heir.confidence) 
    print(largest)



