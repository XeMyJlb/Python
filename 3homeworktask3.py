# 3 - Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

# *Пример:*

# - [1.1, 1.2, 3.1, 5.567, 10.003] => 0.564 или 564
inputNumbers = input("Введите элементы списка из вещественных чисел: ")
list = inputNumbers.replace(" ", "").split(",")

fractalList = []

for element in list:
    fractalElements = str(float(element)).split(".")
    if fractalElements[1] != '0':
        fractalList.append(fractalElements[1])

totalFractalList = []
for index in range(len(fractalList)):
    fractalList[index] = "0." + fractalList[index]

maxValue = float(fractalList[0])
minValue = float(fractalList[0])

for element in fractalList:
    if float(element) > float(maxValue): maxValue = float(element)
    if float(element) < float(minValue): minValue = float(element)

print(f"Разница равна {maxValue - minValue}")