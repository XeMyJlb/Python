# '''Задайте натуральное число N. Напишите программу, 
# которая составит список простых множителей числа N.
# Пример: при N = 12 -> [2, 3]'''

from functions import inputNumbers

def simpleNumber(number):
    for i in range(2, number):
        if number % i == 0:
            return False

    return True

number = inputNumbers("Введите число: ")

def denominator(num):
    denominatorsList = []
    for i in range(2, num):
        if num % i == 0 and simpleNumber(i): 
            denominatorsList.append(i)
    return denominatorsList

print(simpleNumber(number))
print(denominator(number)) 