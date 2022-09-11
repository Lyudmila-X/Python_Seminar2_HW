# Сбор черники

n = int(input('Введите кол-во кустов: '))
print ('Введите количество ягод на каждом кусте: ')
berries = list()
for i in range(n):
    berries.append(int(input()))
max = 0
for i in range(-1, len(berries)-1):
    sum = berries[i-1] + berries[i] + berries[i+1]
    if sum > max:
        max = sum
print (f'Максимальное количество ягод = {max}')
