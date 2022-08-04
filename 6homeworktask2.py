# 2- Найти сумму чисел списка стоящих на нечетной позиции

from functools import reduce


numbers = [1, 2, 3, 4, 5, 6, 7, 8]


def negativeSum(list):
    return reduce(lambda a, b: a+b, map(lambda x: x[1], (filter(lambda x: x[0] % 2 != 0, enumerate(list)))))


print(negativeSum(numbers))
