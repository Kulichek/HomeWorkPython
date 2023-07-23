# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом.
# Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной. 
# Выведите минимальное количество монет, которые нужно перевернуть
from random import randint                     
# генерируем случайный порядок расположения монеток
n = int(input('Введите количество монеток: '))
coins = ""
for i in range(n):
    if randint(0,1) == 0:
        coins += "H"
    else:
        coins += "T"
print("порядок расположения монеток:",coins)

heads = coins.count('H')
tails = n - heads

if heads < tails:
    print("Минимальное количесвто монет, которое нужно перевернуть:", heads)
else:
    print ("Минимальное количесвто монет, которое нужно перевернуть:", tails)    
