# Найдите сумму цифр трехзначного числа.

x = (input('Введите ваше трехзначное число: '))
while len(x)!=3:
    x = (input('Введите ТРЁХЗНАЧНОЕ число: '))
x = int(x)
summa = x//100 + (x%100)//10 + (x%100)%10

print(summa)