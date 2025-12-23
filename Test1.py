import pprint

field = [
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 5, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
]


# def moving_right():
#    for row in range(5):
#        if 5 in field[row]:
#            c = field[row].index(5)
#            if c != 7:
#                field[row][c + 1] = 5
#                field[row][c] = 0

def moving_left():
    for row in range(5):
        if 5 in field[row]:
            c = field[row].index(5)
            if c != 0:
                field[row][c - 1] = 5
                field[row][c] = 0


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