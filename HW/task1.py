# На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. 
# Определите минимальное число монеток, которые нужно перевернуть, 
# чтобы все монетки были повернуты вверх одной и той же стороной.

n = int(input('Введите количество монеток: '))
print("Введите значения стороны каждой монеты: ")
coins = []
for i in range(n):
    coins.append(int(input()))
zero = coins.count(0)
one = coins.count(1)
print("количество монет, которые нужно перевернуть = " + str(min(one, zero)))
