# x = int(input('Введите номер Вашего билета: '))
# summa1 = x//100000 + (x%100000)//10000 + ((x%100000)%10000)//1000
# summa2 = (((x%100000)%10000)%1000)//100 + ((((x%100000)%10000)%1000)%100)//10 + ((((x%100000)%10000)%1000)%100)%10

# if summa1 == summa2:
#     print('Поздравляю! У Вас счастливый билетик!')
# else:
#     print(':( К сожалению в этот раз Вам не повезло, билет не счатливый :(')

x = input('Введите номер Вашего билета: ')

if len(x) != 6:
    print('Не повезло, билетик не счастливый.')
else:
    i=0
    summa1=0

    while i <= 2:
        y = int(x[i])
        summa1 = summa1 + y
        i +=1

    i = 3
    summa2=0

    while i <= 5:
        y = int(x[i])
        summa2 = summa2 + y
        i +=1

    if summa1 == summa2:
        print('Поздравляю! У Вас счастливый билетик!')
    else:
        print(':( К сожалению в этот раз Вам не повезло, билет не счатливый :(')