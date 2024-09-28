import random

class car:
    def __init__(self, brand, model, year, price):
        self._brand = brand
        self._model = model
        self.year = year
        self.price = price

    @property
    def brand(self):
        brand_names = {1 : 'BMW', 2 : 'Toyota', 3 : 'Audi', 4 : 'Honda', 5 : 'Ferrari'}
        try:
            return brand_names[self._brand]
        except:
            print("That brand doesn't exist")







Car1 = car(random.randint(1, 8), random.randint(1, 10), 
           random.randint(2000, 2022), random.randint(150000, 1000000))

print(Car1.brand)
