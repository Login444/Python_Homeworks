n = int(input('Введите колличество кустов на грядке: '))
import random
blueberries = list(random.randint(1,10) for i in range(n))
print(f'Ваш куст: {blueberries}')
bush_list = list(i for i in range(n))


for i in range(n):
    if i != n-1 and i != 0:
        bush_list[i] = blueberries[i-1] + blueberries[i] + blueberries[i+1]
    elif i == 0:
        bush_list[i] = blueberries[n-1] + blueberries[i] + blueberries[i+1]
    elif i == n-1:
        bush_list[i] = blueberries[i-1] + blueberries[i] + blueberries[0]


maximum = 0

for i in range(len(bush_list)):
    if bush_list[i] > maximum:
        maximum = bush_list[i]
print(f'Максимальное число ягод, которое может собрать за один заход собирающий модуль равно {maximum}')