a = int(input('Введите число "a": '))
b = int(input('Введите число "b": '))

def sum_nums(x,y):
    if y == 0:
        return x
    if y < 0:
        return sum_nums(x,y+1)-1
    return sum_nums(x,y-1) + 1

print(sum_nums(a,b))