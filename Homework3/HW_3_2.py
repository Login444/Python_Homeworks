n = int(input('Введите колличество элементов в списке: '))
list = [i for i in range(1,n+1)]
print(list)
x=int(input('Введите число которое ищем: '))
min_dif=0
minimum = 0
for i in range(0,len(list)):
    dif = x - list[i]
    if list[i] == x:
        minimum = list[i]
    elif i == len(list):
            if list[i-1]>list[i]:
                minimum = list[i-1]
            else:
                minimum = list[i]
    elif min_dif == 0:
         min_dif = dif
         minimum = list[i]
    elif dif < min_dif:
         min_dif = dif
         minimum = list[i]
print(minimum)