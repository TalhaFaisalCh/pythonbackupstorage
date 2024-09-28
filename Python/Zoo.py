import random
import time
class Animal:
    def __init__(self, species, name, age, hunger, thirst, hygiene, health, happiness):
        self.species = species
        self.name = name
        self.age = age
        self.hunger = hunger
        self.thirst = thirst
        self.hygiene = hygiene
        self.health = hunger + thirst + hygiene
        self.happiness = int(hunger + ((thirst + hygiene)/20) + (health/2) - (age*3.141592653589793238462643383279502884197))
    def feeding(self):
        self.hunger += 5
        self.happiness = int(self.hunger + ((self.thirst + self.hygiene)/20) + (self.health/2) - (self.age*3.141592653589793238462643383279502884197))
    def drinking(self):
        self.thirst += 5
        self.happiness = int(self.hunger + ((self.thirst + self.hygiene)/20) + (self.health/2) - (self.age*3.141592653589793238462643383279502884197))
    def playing(self):
        self.happiness+= 5
    def provide_medical_care(self):
        self.hygiene += 8
        self.hunger += 2
        self.thirst += 2
        self.happiness = int(self.hunger + ((self.thirst + self.hygiene)/20) + (self.health/2) - (self.age*3.141592653589793238462643383279502884197))

class Lion(Animal):
    def __init__(self, species, name, age, hunger, thirst, hygiene, health, happiness):
        super().__init__(species, name, age, hunger, thirst, hygiene, health, happiness)
class Elephant(Animal):
    def __init__(self, species, name, age, hunger, thirst, hygiene, health, happiness):
        super().__init__(species, name, age, hunger, thirst, hygiene, health, happiness)
class Giraffe(Animal):
    def __init__(self, species, name, age, hunger, thirst, hygiene, health, happiness):
        super().__init__(species, name, age, hunger, thirst, hygiene, health, happiness)
class Enclosure:
    def __init__(self, animalenclosed, size, clean, food_supply):
        self.animalenclosed = animalenclosed
        self.size = size
        self.clean = clean
        self.food_supply = food_supply
        self.animal_inside_enclosure = []

class Zookeeper:
    def __init__(self, name, specieskeeper, age, gender):
        self.name = name
        self.specieskeeper = specieskeeper
        self.age = age
        self.gender = gender
    def givefood():
        pass

simba = Lion('Lion', 'Simba', 5, 100, 100, 100, 99999, 50)
dumbo = Elephant('Elephant', 'Dumbo', 7, 100, 100, 100, 99999, 60)
melman = Giraffe('Giraffe', 'Melman', 12, 100, 100, 100, 99999, 40)

lionenclosure = Enclosure('Lion', 50, 100, 20)

lionenclosure.animal_inside_enclosure.append(simba)
print(len(lionenclosure.animal_inside_enclosure))
kevin = Zookeeper('Kevin', lionenclosure, 25, 'male')
print(kevin.specieskeeper.animal_inside_enclosure[0].name)