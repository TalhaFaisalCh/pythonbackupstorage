import random
import time

def get_USERchoice(LIST):
    USERchoice = ''
    while USERchoice not in LIST:
        USERchoice = input("What do you want to play?: ").lower()
    return USERchoice

def get_SYSchoice(LIST):
    SYSchoice = LIST[random.randint(0, 2)]
    return SYSchoice

def choose_winner(USERchoice, SYSchoice):
    if (USERchoice == 'rock' and SYSchoice == 'scissor') or \
    (USERchoice == 'paper' and SYSchoice == 'rock') or \
    (USERchoice == 'scissor' and SYSchoice == 'paper'):
        return 'YOU WIN!', 1 
        

    elif (USERchoice == SYSchoice):
        return 'TIE!', 0

    else:
        return 'CPU WON!', -1
        

def WIN_all(USERscore, SYSscore):
    if USERscore > SYSscore:
        return 'USER WINS!'
    else:
        return 'CPU WINS!'



if __name__ == '__main__':
    print('=================[INSRT TEXT]=================')

