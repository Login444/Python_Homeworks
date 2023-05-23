# Задача 34:  Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм. 
# Поскольку разобраться в его кричалках не настолько просто, насколько легко он их придумывает, 
# Вам стоит написать программу. Винни-Пух считает, что ритм есть, если число слогов 
# (т.е. число гласных букв) в каждой фразе стихотворения одинаковое. 
# Фраза может состоять из одного слова, если во фразе несколько слов, 
# то они разделяются дефисами. Фразы отделяются друг от друга пробелами. 
# Стихотворение  Винни-Пух вбивает в программу с клавиатуры. 
# В ответе напишите “Парам пам-пам”, если с ритмом все в порядке
# и “Пам парам”, если с ритмом все не в порядке

def vowels(poem):
    phrases = []
    for i in range(len(poem)):
        count = 0
        for j in range(len(poem[i])):
            if poem[i][j] not in "йцукенгшщзхъэждлорпавыфячсмитьЙЦУКЕНГШЩЗХЪЭЖДЛОРПАВЫФЯЧСМИТЬБЮЁё":
                return print('Винни пух не знает английский!')
            else:
                if poem[i][j] in "ёуеыаоэяиюЁУЕЫАОЭЯИЮ":
                    count+=1
        phrases.append(count)
    return phrases

def rythm(list):
    flag = True
    for i in range(1,len(list)):
        if list[0] == list[i]:
            flag = True
        else:
            flag = False
            break
    if flag == True:
        print('Парам пам-пам')
    else:
        print('Пам парам')

rythm(vowels(input('Введите стихотворение: ').split()))