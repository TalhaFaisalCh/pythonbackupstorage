from abc import ABC, abstractmethod
import random
import time
class car:
    def __init__(self, name, speed, acceleration, handling, brakes):
        self.name = name
        self.speed = speed
        self.acceleration = acceleration
        self.handling = handling
        self.brakes = brakes

#class race:
 #   track_parts = ['straight', 'easy_turn', 'medium_turn', 'hard_turn', 'climb', 'fall']
  #  def easy():
   #     c = CitySprint()
    #def medium():
     #   a = AlpinoAccent()
    #def hard():
     #   m = MysticPeaks()

class race:
    def race():
        player_interval = 0
        e1_interval = 0
        e2_interval = 0
        e3_interval = 0
        e4_interval = 0
        e5_interval = 0

        while True:
            print('go')

track_parts = ['straight', 'easy_turn', 'medium_turn', 'hard_turn', 'climb', 'fall']
McLaren = car('McLaren' ,10, 7, 7, 10) 
Ferrari = car('Ferrari', 8, 10, 7, 7)
Toyota = car('Toyota', 5, 8, 10, 9)
Ford = car('Ford', 9, 6, 8, 8)
Skyline = car('Skyline', 8, 6, 9, 9)
Lamborgini = car('Lamborgini', 9, 8, 6, 8)
Honda = car('Honda', 7, 6, 7, 10)

class Track(ABC):
    @abstractmethod
    def display():
        pass
class CitySprint(Track):
    def display():
        print('You have selected City sprint')
class AlpinoAccent(Track):
    def display():
        print('You have selected Alpino Accent')
class MysticPeaks(Track):
    def display():
        print('You have selected Mystic Peaks')

CARS = [McLaren, Ferrari, Toyota, Ford, Skyline, Lamborgini, Honda]
TRACKS = [CitySprint(), AlpinoAccent(), MysticPeaks()]
for i in range(len(CARS)):
    print(CARS[i].name)
choice = int(input('Which car to select?: '))
player=CARS[choice - 1]
choice = int(input('Which difficulty? Easy[1], Medium[2], Hard[3]: '))

track = []

if choice == 1:
    for i in range(30):
        n = random.randint(0, 2)
        
        rng = random.randint(0, 1)
        if rng == 1:
            n = 0
        track.append(n)
if choice == 2:
    for i in range(45):
        n = random.randint(0, 3)
        
        rng = random.randint(0, 6)
        if rng == 1:
            n = 0
        track.append(n)

if choice == 3:
    n = random.randint(0, 5)
        
    rng = random.randint(0, 6)
    if rng == 1 or rng == 0:
        n = 3
    if rng == 2:
        n = 4
    track.append(n)

e1 = CARS[random.randint(0, len(CARS)-1)]
e2 = CARS[random.randint(0, len(CARS)-1)]
e3 = CARS[random.randint(0, len(CARS)-1)]
e4 = CARS[random.randint(0, len(CARS)-1)]
e5 = CARS[random.randint(0, len(CARS)-1)]