'''
1. После запуска предлагает пользователю ввести целые неотрицательные числа,
разделенные любым не цифровым литералом (пробел, запятая, %, буква и т.д.).
2. Получив вводные данные, выделяет полученные числа, суммирует их,
и печатает полученную сумму.
'''
inputString = input()
c = ''
a = []
positiveInt = False  # если false то число положительное
readInteger = True  # если true то считывается число, иначе false начало строки
for i in inputString:
    '''
    если встретилось число то склеиваем строку из встречающихся цифр
    иначе преобразуем скленную строку в цисло, учитываем знак и записываем в список
    '''
    if '0' <= i <= '9':
        readInteger = True
        c = c+i
    else:
        readInteger = False
    if ((not(readInteger)) & (c != '')):
        if positiveInt:
            a.append(-int(c))
            positiveInt = False
            c=''
        else:
            a.append(int(c))
            positiveInt = False
            c=''
    else:
        pass
    '''
    если встретился занк '-', то записываем это в флаг,
    так как потенциальное число может быть отрицательным
    '''
    if i == '-':
        positiveInt = True
    else:
        if not(readInteger):
            positiveInt = False

if ((c != '')):
    if positiveInt:
        a.append(-int(c))
        positiveInt = False
        c=''
    else:
        a.append(int(c))
        positiveInt = False
        c=''
print(sum(a))

