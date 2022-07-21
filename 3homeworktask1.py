# 1 - Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
InputNumbers = input("Задайте список из нескольких целых чисел\n: ")
list = InputNumbers.replace(" ", "").split(",")
summ = 0

for index in range(len(list)):
    if index % 2 != 0:
        summ += int(list[index])

print(summ)
