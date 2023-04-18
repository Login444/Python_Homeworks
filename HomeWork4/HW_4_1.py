# Даны два неупорядоченных набора целых чисел (может быть, с повторениями). 
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n — кол-во элементов первого множества. 
# m — кол-во элементов второго множества. Затем пользователь вводит сами элементы множеств.

n = int(input('Введите колличество элемнтов 1го множества: '))
m = int(input('Введите колличество элементов 2го множества: '))
import random
n_numbers = {random.randint(0,10) for i in range(n)}
print(n_numbers)
m_numbers = {random.randint(0,10) for i in range(m)}
print(m_numbers)

a = n_numbers.intersection(m_numbers)
print(a)
print(sorted(a))

# a = list(a)
# tmp = 0
# for i in range(len(a)):
#     for k in range(len(a)):
#         if a[i] < a[k]:
#             tmp=a[i]
#             a[i]=a[k]
#             a[k]=tmp
# print(a)