# Напишите программу, которая на вход принимает два числа A и B, 
# и возводит число А в целую степень B с помощью рекурсии.

a = int(input('Введите число "a": '))
b = int(input('Введите число "b": '))

def pow(x,y):
    if y == 0:
        return 1
    if y < 0:
        return pow(x,y+1) * 1 / x
    return pow(x,y-1)*x

print(pow(a,b))