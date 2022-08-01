# 2- Создайте программу для игры с конфетами человек против человека.

# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. Тот, кто берет последнюю конфету - проиграл.

# a) Добавьте игру против бота

# b) Подумайте как наделить бота ""интеллектом""

from random import randint

def playerTurn(candiesCouts, maxСount):
    global last_step
    playerInput = int(input("Take from 1 to 28 candies: "))
    while not (0 < playerInput <= maxСount):
        if(playerInput <= 0):
            print("Take at least one candy!!")
            playerInput = int(input("How many candies we take?: "))
        elif playerInput > maxСount:
            print(f"You can't carry that much candy! Max per turn {maxСount}!")
            playerInput = int(input("How many candies we take? "))
    else:
        if playerInput > candiesCouts:
            playerInput = candiesCouts
    last_step = playerInput
    return candiesCouts - playerInput



def Ostatok(candiesCounts, max, lastRound):
    candi = max + 1 - lastRound

    if candiesCounts > max and (1 < candiesCounts / max < 2):
        print(candiesCounts - (max + 1))
        candi = candiesCounts - (max + 1) 
    if candi > candiesCounts or candiesCounts <= max:
        candi = candiesCounts
    return candi

candiesCounts = 90
maxCount = 28

player = randint(0, 1)

last_step = 0

while(candiesCounts > 0):
    print(f"Player turn {player + 1}")
    if player == 0: 
        candiesCounts = playerTurn(candiesCounts, maxCount)
        if(candiesCounts > 0):
            player += 1
    else:
            candiesCounts = playerTurn(candiesCounts, maxCount)
            if(candiesCounts > 0):
                player -= 1    
    print(f"Candies {candiesCounts} left ")
else:
    print(f"Player {player + 1} wins!!!")