# '''В текстовом файле удалить все слова, 
# которые содержат хотя бы одну цифру.
# Мама сшила м0не штаны и7з бере9зовой кор45ы 893. -> Мама сшила штаны.'''

text = input("Введите текст: ")

def WordDigit(word):
    for char in word:
        if char.isdigit():
            return True
    return False

def WordsSifting(text):
    words = text.split()
    WordsResult = []
    for word in words:
        if not WordDigit(word):
            WordsResult.append(word)
    return WordsResult

print(WordsSifting(text)) 