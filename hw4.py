s = input()
c = ''
a = []
f = False  # если false то число положительное
inC = True  # если true то считывается число, иначе false начало строки
for i in s:
    '''
    если встретилось число то склеиваем строку из встречающихся цифр
    иначе преобразуем скленную строку в цисло, учитываем знак и записываем в список
    '''
    if '0' <= i <= '9':
    else:
        inC = False
    if ((not(inC)) & (c != '')):
        if f:
            a.append(-int(c))
            f = False
            c=''
        else:
            a.append(int(c))
            f = False
            c=''
    else:
        pass
    '''
    если встретился занк '-', то записываем это в флаг,
    так как потенциальное число может быть отрицательным
    '''
    if i == '-':
        f = True
    else:
        if not(inC):
            f = False

if ((c != '')):
    if f:
        a.append(-int(c))
        f = False
        c=''
    else:
        a.append(int(c))
        f = False
        c=''
print(sum(a))

