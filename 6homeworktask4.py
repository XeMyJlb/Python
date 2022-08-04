# 4- Определить, позицию второго вхождения строки в списке либо сообщить, что её нет.
# Примеры
# список: ["qwe", "asd", "zxc", "qwe", "ertqwe"], ищем: "qwe", ответ: 3
# список: ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"], ищем: "йцу", ответ: 5
# список: ["йцу", "фыв", "ячс", "цук", "йцукен"], ищем: "йцу", ответ: -1
# список: ["123", "234", 123, "567"], ищем: "123", ответ: -1
# список: [], ищем: "123", ответ: -1

list = ["qwe", "asd", "zxc", "qwe", "ertqwe"]
desired = 'qwe'


def second_in(list, desired):
    count = 0
    for i, element in enumerate(list):
        if element == desired:
            count += 1
            if count == 2:
                break
    if count > 0:
        return i
    else:
        return -1


print(second_in(list, desired))
