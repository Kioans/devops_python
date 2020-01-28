s = input("Введите строку ")
ls = s.split(' ')
a = list(set(ls))
for i in a:
    print(i, end=' ')
