import random
import time
from FunctionsONLYasModules import read_file
Names = read_file('first-names.txt')
class customer:
    def __init__(self, name, Type, manipulation_level):
        self.name = Names[name]
        self._Type = Type
        self.manipulation_level = manipulation_level
    

    @property
    def Type(self):
        if self._Type <= 11:
            return 'shopper'
        else:
            type_names = {12: "Gambler", 13: "Tax_official", 14: "karen", 15: "scammer", 16: "enterpreneur"}
            return type_names[self._Type]
        
    @Type.setter
    def Type(self, value):
        print(str(value)+"gfhjghfdjkghjfkhgjkfdhgjkfdhgk")
        if (value < 13):
            raise ValueError("Not allowed")
        self._Type = value

c1 = customer(5,  5, 10)
print(c1.name)
print(c1.Type)
        


        

# day = 0
# stock = ['bread', 'iphone', 'lays', 'pickle', 'paper']
# amount = [30, 5, 16, 99 ,120]

# # Cost Per Item
# CPI = [10, 1000, 15, 500, 20] 

# money = 9000

# while money >= 0:
#     choice = int(input('What are you going to do: Start_day[1], Buy_Stock[2]: '))
#     if choice == 2:
#         buy = input('Buy what?: ').lower()
#         print(buy)
#         print(amount)
#         print(money)
#         if buy in stock:
#             index = stock.index(buy)
#             buy = int(input('How much?: '))
#             A = CPI[index] * buy
#             if money - A <= 0:
#                 print("Trasaction failed! You'd be broke.")
#             else:
#                 money -= A
#                 amount[index] += buy
#                 print(amount)
#                 print(money)
    


#     if choice == 1:
#         print('Lets get started!')
#         time.sleep(1)
#         day += 1
#         print('day', day)
#         for i in range(10):
#             customerRNG = customer(random.randint(0, len(Names) - 1), random.randint(1, 16), random.randint(0, 100))
#             # customerRNG.Type = 12
#             customerIN = True
#             print(customerRNG.name)
#             print(customerRNG.Type)
#             print(customerRNG.manipulation_level)

#             #while customerIN:
#                 #if customer(Type)


