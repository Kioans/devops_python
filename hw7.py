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
dictGID = {}
dictGroupUid = {}
answShell = '( '
answUID = ''
for line in f:
    sline = line.split(":")
    listUID = []
    if len(sline) >= 6:
        shell = sline[6].strip("\n")
        dictShell.update({shell: dictShell.get(shell, 0)+1})
        dictUID[sline[0]] = sline[2]  # записвыем словарь "Имя пользователя": UID
        dictGID[sline[0]] = sline[3]  # записвыем словарь "Имя пользователя" : GID
#print("Количество пользователей, использующих все имеющиеся интерпретаторы-оболочки")
for i in dictShell:
    answShell += ' ' + i + ' - ' + str(dictShell.get(i)) + ' ;'
answShell += ' )'
f.close()


fg = open("/etc/group", "r")
dict_groups_name = {}
group_id_name = {}
list_etc_group =[]
for line in fg:
    usersUID = ''
    list_etc_group.append(line.strip('\n').split(":"))
    groupName = line.split(":")[0]  # получаем имя группы
    groupID = line.split(":")[2]
    usersName = line.split(":")[3].strip("\n").split(",")  # получаем имена пользователей принадлежащих просматриваемой группе
    dict_groups_name[groupID] = groupName

for name in dictUID: #итерируемся по именам пользователей и групп из passwd
    groupName = dict_groups_name[dictGID[name]]
    answUID += f'uid={dictUID[name]}({name}) gid={dictGID[name]}({groupName}) ' \
f'groups={dictGID[name]}({groupName}),'
    for uig in list_etc_group:
        if name in uig:
            if uig[0] != name:
                answUID += f'{uig[2]}({uig[0]}),'
    answUID += '\n'
fg.close()

f = open("output.txt","w")
f.write("Количество пользователей, использующих все имеющиеся интерпретаторы-оболочки\n")
f.write(answShell + "\n\n")
f.write("Для всех групп в системе - UIDы пользователей состоящих в этих группах.\n")
f.write(answUID + "\n")
f.close()









