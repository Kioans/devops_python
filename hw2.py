s = input("Введите строку ")
ls = s.split(' ')
cleandict = {i: ls.count(i) for i in ls}
for key in cleandict:
    print(key, end=' ')
