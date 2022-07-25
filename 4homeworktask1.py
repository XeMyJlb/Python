# '''Вычислить число c заданной точностью d. Число Пи не просто обрезать с math.pi, а вычислить,
#  используя формулы: Нилаканта, ряды Тейлора, серию Ньютона или серию Чудновских.'''

from functions import inputNumbers


def Nilakantha(d):
    i = 0

    pi = 3

    while i <= d:
        p = (4 / ((2 + i * 2) * (3 + i * 2) * (4 + i * 2)))

        if i % 2 == 0:
            pi += p
        else:
            pi -= p
        i += 1
    return pi


d = inputNumbers("Введите число: ")
print(Nilakantha(d))
