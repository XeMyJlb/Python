# 3- Найти расстояние между двумя точками пространства(числа вводятся через пробел)

import math


def positionCheck():
    positions = input("Введите позиции для 4х точек: x1 y1 x2 y2): ")
    while 1:
        positionTest = positions.split(" ")
        positions = list(filter(lambda x: x.isdigit(), positionTest))
        if len(positions) != 4:
            positions = input(f"Четыре точки!")
        else:
            break
    return positions


def rangeBetweenDots():
    positions = positionCheck()
    return math.ceil(((int(positions[0]) - int(positions[2]))**2 + (int(positions[3])-int(positions[1]))**2)**0.5)


print(rangeBetweenDots())
