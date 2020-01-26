while True:
    mx = 1
    v = 0
    s = input("Введите строку: ")
    s.lower() #приводим слова к нижнему регистру
    a = s.split() # создаём список из введённой строки
    dictionary = {}

    for i in a:
        if dictionary.get(i) is None: #если в словаре нет ключа i то добавляем его со значением 1
            dictionary.update({i: 1})
        else: # если в словаре есть ключ, то увеличиваем значение на 1
            v = dictionary.get(i) + 1
            dictionary.update({i: v})
        if mx < v:
            mx = v

    for key,value in dictionary.items():
        if value == mx:
            print(f"{value} - {key}")
