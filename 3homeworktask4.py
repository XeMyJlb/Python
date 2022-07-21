# 4 - Напишите программу, которая будет преобразовывать десятичное число в двоичное.

# *Пример:*

# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

inputNumbers = int(input("Введите ваше число: "))
 
rem = ''
 
while inputNumbers > 0:
    rem = str(inputNumbers % 2) + rem
    inputNumbers = inputNumbers // 2
 
print(rem)