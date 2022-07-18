# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
numbers = int(input('Введите число: '))


def multiplication(n):
    factorial = 1
    list = []
    for i in range(1, n+1):
        factorial *= i
        list.append(factorial)
    return list


print(multiplication(numbers), end=' ')
