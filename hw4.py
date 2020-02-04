'''
1. После запуска предлагает пользователю ввести целые неотрицательные числа,
разделенные любым не цифровым литералом (пробел, запятая, %, буква и т.д.).
2. Получив вводные данные, выделяет полученные числа, суммирует их,
и печатает полученную сумму.
'''
inputString = input("Введите целые неотрицательные числа: ")
integer = ''
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
        chislo = chislo + i
    else:
        readInteger = False
    if ((not(readInteger)) & (chislo != '')):
        if positiveInt:
            a.append(-int(chislo))
            positiveInt = False
            chislo= ''
        else:
            a.append(int(chislo))
            positiveInt = False
            chislo= ''
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

if ((chislo != '')):
    if positiveInt:
        a.append(-int(chislo))
        positiveInt = False
        chislo= ''
    else:
        a.append(int(chislo))
        positiveInt = False
        chislo= ''
print(sum(a))

