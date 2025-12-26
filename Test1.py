import pprint

field = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
]


def moving_right():
    for row in range(len(field)):
        if 5 in field[row]:
            c = field[row].index(5)
            if c != len(field[row]) - 1:
                field[row][c + 1] = 5
                field[row][c] = 0
                break


def moving_left():
    for row in range(len(field)):
        if 5 in field[row]:
            c = field[row].index(5)
            if c != 0:
                field[row][c - 1] = 5
                field[row][c] = 0
                break


def moving_down():
    for row in range(len(field)):
        if 5 in field[row]:
            c = field[row].index(5)
            if row < len(field) - 1:
                field[row + 1][c] = 5
                field[row][c] = 0
                break


moving_down()
pprint.pprint(field)

"""
создать репоситорий для проекта
сделать движение влево
сделать движение вниз
подготовить базовый код для аркейда(дипсик)
найти спрайты для 2 объектов
q learning

докер
mysql
"""
