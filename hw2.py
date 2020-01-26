s = input("Введите строку ")
print("Ввведённая строка = ", s)
ls = s.split(' ')
print("Список составленный и введённой строки = ", ls)
a = list(set(ls))
print("Список элементов без дубликатов = ", end=' ')
for i in a:
    print(i, end=' ')

