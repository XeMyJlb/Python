# 2 - Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# *Пример:*

# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

inputNumbers = input("Введите целые числа: ")
list = inputNumbers.replace(" ", "").split(",")

if len(list) % 2 == 0:
    lenghtList = len(list)//2
else:
    lenghtList = len(list) // 2 + 1

for index in range(lenghtList):
    print(int(list[index])*int(list[len(list) - 1 - index]))
