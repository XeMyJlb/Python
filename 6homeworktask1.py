# 1- Определить, присутствует ли в заданном списке строк, некоторое число
import math



def numberInList(userList, number):
    return list(filter(lambda element: str(number) in element, userList))

user_lst = ["пе4енька", "варенье", "во", "рту", "меня"]
print(numberInList(user_lst, 4))
