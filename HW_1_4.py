n = int(input('Введите размер шоколадки по горизонтали: '))
m = int(input('Введите размер шоколадки по вертикали: '))
k = int(input('Введите сколько долек хотите отломить: '))
x = (n*m)-k

if x > 0 and x%2 == 0:
    print('У вас осталась плитка из',x,'долек' )
else:
    print('Так поделить не получится!')