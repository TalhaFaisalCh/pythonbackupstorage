from RockPaperScissors import get_USERchoice
from RockPaperScissors import get_SYSchoice
from RockPaperScissors import choose_winner
from RockPaperScissors import WIN_all


USERscore = 0
SYSscore = 0
LIST = ['rock','paper','scissor']

while True:
    USERchoice = get_USERchoice(LIST)

    SYSchoice = get_SYSchoice(LIST)
    print('CPU chose', SYSchoice)

    result, point = choose_winner(USERchoice, SYSchoice)
    
    print(result)
    
    if point == 1:
        USERscore += 1
    
    elif point == -1:
        SYSscore += 1
    
    point = 0

    if USERscore == 5 or SYSscore == 5:
        break

WIN_all(USERscore, SYSscore)
