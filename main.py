from random import randint


def start():
    print('''
    #################### Игра "15 спичек" ################
    Всего в куче 15 спичек. Каждый игрок по очерди берёт от 
    ################### 1 до 3 спичек. ####################
    Выигрывает тот, кто заберёт последние спички из кучи.
    ''')
#

def get_turn():
    print('''
    Введите 0, чтобы ходить первым.
    Введите 1, чтобы первым ходил компьютер.
    Введите 2, чтобы очерёдность хода выбиралась случайно.
    ''')
    turn = input()
    while not (turn == '0' or turn == '1' or turn == '2'):
        print('Ошибка! Проверьте корректность вашего ввода. Вы должны ввести 0, 1 или 2.')
        turn = input()
    if turn == '2':
        turn = randint(0, 1)
    return int(turn)
