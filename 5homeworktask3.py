# 3-Создайте два списка — один с названиями языков программирования, другой — с числами от 1 до длины первого.
# ['python', 'c#']
# [1,2]
# Вам нужно сделать две функции: первая из которых создаст список кортежей, состоящих из номера и языка, написанного большими буквами.
# [(1,'PYTHON'), (2,'C#')]

from functools import reduce


def creatingArrayOfTuples(lstOfNumbers, lstOfLangueges):
    arrayOfTuples = list(zip(lstOfNumbers, list(
        map(lambda language: language.upper(), lstOfLangueges))))
    return arrayOfTuples


def filteredArrayOfTuples(arrayOfTuples):
    arrayOfFilteredTuples = []
    for i in range(len(arrayOfTuples)):
        count = 0
        for j in arrayOfTuples[i][1]:
            count += ord(j)
        if count % arrayOfTuples[i][0] == 0:
            buf = list(arrayOfTuples[i])
            buf[0] = count
            arrayOfTuples[i] = tuple(buf)
            arrayOfFilteredTuples.append(arrayOfTuples[i])
    print(f'Filtered tuples - {arrayOfFilteredTuples}')
    sum = reduce(lambda s, y: s + y[0], arrayOfFilteredTuples, 0)
    return sum


languages = ['Python', 'C#']
numbers = list(range(1, len(languages) + 1))
tuples = creatingArrayOfTuples(numbers, languages)
print(f'List of tuples - {tuples}')
print(f'Sum of numbers - {filteredArrayOfTuples(tuples)}')
