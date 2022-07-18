# 1 - Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

# *Пример:*

# - 6782 -> 23
# - 0,56 -> 11
def EnterFloatNumber():
    while(True):
        try:
            number = input("Введите число: ")
            float(number)
            break
        except ValueError:
            print("Вы ввели что-то не то: ")
    return number


def SummDigit(number: any):
    sum = 0
    num = str(number).replace(".", "")
    for i in num:
        sum += int(i)
    return sum


number = EnterFloatNumber()

print(f"Сумма = {SummDigit(number)}")
