# Определить индексы элементов массива (списка), значения которых принадлежат 
# заданному диапазону (т.е. не меньше заданного минимума и не больше заданного максимума)

import random

list = [random.randint(-15,15) for i in range(random.randint(10,20))]

print(list)

a = int(input('Задайте минимум: '))
b = int(input('Задайте максимум: '))

list_index = []

for i in range(len(list)):
    if a <= list[i] <= b:
        list_index.append(i)
print(list_index)