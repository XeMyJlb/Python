# 2- Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).
x = float(input("Введите переменную х:\n "))
y = float(input("Введите переменную у:\n "))
if x > 0 and y > 0:
    print("Вы в 1 четверти")
elif x < 0 and y > 0:
    print("Вы в 2 четверти")
elif x < 0 and y < 0:
    print("Вы в 3 четверти")
elif x > 0 and y < 0:
    print("Вы в 4 четверти")
elif x == 0 or y == 0:
    print("X ≠ 0 и Y ≠ 0")