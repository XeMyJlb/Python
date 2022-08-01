# # 1- Напишите программу, удаляющую из текста все слова, содержащие ""абв"".
# 'абвгдейка - это передача' = >" - это передача"

exceptionWord = input("Введите исключающие символы одной строкой: ")
word = 'абвгдейка - это передача'.split()
print(f"Оригинальный текст: {' '.join(word)}")
result = [i for i in word if exceptionWord not in i]
print(f"Текст без слова {exceptionWord}: {' '.join(result)}")