# Задача 36: 
# Напишите функцию print_operation_table(operation, num_rows=6, num_columns=6), которая принимает в качестве аргумента функцию, 
# вычисляющую элемент по номеру строки и столбца. Аргументы num_rows и num_columns указывают число строк и столбцов таблицы, 
# которые должны быть распечатаны. Нумерация строк и столбцов идет с единицы (подумайте, почему не с нуля). 
# Примечание: бинарной операцией называется любая операция, у которой ровно два аргумента, как, например, у операции умножения.
import random

def operation(rows,columns):
    matrix = []
    for i in range(rows):
        a =[]
        for j in range(columns):
            a.append(random.randint(1,9))
        matrix.append(a)
    
    for i in range(rows):
        for j in range(columns):
            print(matrix[i][j], end = " ")
        print()
    return matrix


def print_operation_table(matrix, row, column):
    res = matrix[row-1][column-1]
    print(res)

num_rows = int(input('Введите колличество строк: '))
num_columns = int(input('Введите колличество столбцов: '))

find_row = int(input('Введите в какой строке ищем: '))
find_column = int(input('Введите в каком столбце ищем: '))

print_operation_table(operation(num_rows, num_columns), find_row, find_column)
