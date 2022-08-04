# 5- Найти произведение пар чисел в списке. Парой считаем первый и последний элемент, второй и предпоследний и т.д.

list = [7, 4, 5, 10, 2]


def pairsProduct(list):
    return [list[i] * list[len(list)-1 - i] for i in range(len(list)//2 + len(list) % 2)]

print(pairsProduct(list))
