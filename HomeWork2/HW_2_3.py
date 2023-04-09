# Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.

n = int(input('Введите ваше число: '))

for i in range(n):
    result=2**i
    if result <=n:
        print(result)