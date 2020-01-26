'''
Напишите программу, которая читает данные из файлов
/etc/passwd и /etc/group на вашей системе и выводит
следующую информацию в файл output.txt:
1. Количество пользователей, использующих все имеющиеся
интерпретаторы-оболочки.
( /bin/bash - 8 ; /bin/false - 11 ; ... )
2. Для всех групп в системе - UIDы пользователей
состоящих в этих группах.
( root:1, sudo:1001,1002,1003, ...)

'''
f = open("/etc/passwd", "r")
dictShell = {}
dictUID = {}
dictGroupUid = {}
answShell = '( '
answUID = '( '
for line in f:
    sline = line.split(":")
    listUID = []
    if len(sline) >= 6:
        shell = sline[6].strip("\n")
        dictShell.update({shell: dictShell.get(shell, 0)+1})
        dictUID[sline[0]] = sline[2]  # записвыем словарь "Имя пользователя": UID
#print("Количество пользователей, использующих все имеющиеся интерпретаторы-оболочки")
for i in dictShell:
    answShell += ' ' + i + ' - ' + str(dictShell.get(i)) + ' ;'
answShell += ' )'
f.close()


fg = open("/etc/group", "r")
for line in fg:
    usersUID = ''
    groupName = line.split(":")[0]  # получаем имя группы
    usersName = line.split(":")[3].split(",")  # получаем имена пользователей принадлежащих просматриваемой группе
    if (len(usersName) == 0) or (usersName[0] == '\n') or (usersName[0] == ''):
        groupName = ''
        usersName.clear()
    else:
        answUID += ' ' + groupName + ':'
    for un in usersName:  # по имени пользователя принадлежащей просматриваемой группе находим его UID в dictUID
        un = un.strip('\n')
        for i in dictUID:
            if un == i:
                answUID += str(dictUID.get(i)) + ','  # записываем UIDы пользователей принадлежащей группе
    usersName.clear()
answUID += " )"
fg.close()


f = open("output.txt","w")
f.write("Количество пользователей, использующих все имеющиеся интерпретаторы-оболочки\n")
f.write(answShell + "\n\n")
f.write("Для всех групп в системе - UIDы пользователей состоящих в этих группах.\n")
f.write(answUID + "\n")
f.close()









