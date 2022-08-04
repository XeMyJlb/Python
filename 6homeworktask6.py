# 6-Сформировать список из  N членов последовательности.
# Для N = 5: 1, -3, 9, -27, 81 и т.д.

numbers = int(input('Введите длину последовательности: '))


def sequence(n):
    return [(-3) ** i for i in range(0, n)]


print(sequence(numbers))
