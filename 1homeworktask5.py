# 5- Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.

import math
from turtle import distance
from unittest import result

print ('Координаты А')
x1 = int(input('Х1: '))
y1 = int(input('Y1: '))

print ('Координаты B')
x2 = int(input('Х2: '))
y2 = int(input('Y2: '))

distance = math.sqrt((x2 - x1) * (x2 - x1) + (y2 - y1) * (y2 - y1)) 
print(round(distance, 3))