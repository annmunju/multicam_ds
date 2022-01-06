# gbbGame.py

import random

def gbb_game(you_n):
    global com
    com = random.randint(1, 3)

    if com == you_n:
        print('비겼습니다.')
    elif (com == 1 and you_n == 2) or (com == 2 and you_n == 3) or (com == 3 and you_n == 1):
        print('당신이 이겼습니다.')
    else:
        print('컴퓨터가 이겼습니다.')

    print(f'COM : {com}')

def input_num():
    you_n = int(input('YOU 입력(1:가위, 2:바위, 3:보) : '))
    return gbb_game(you_n)

#input_num()