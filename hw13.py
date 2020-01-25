'''
Напишите функцию, которая переводит значения показаний
температуры из Цельсия в Фаренгейт и наоборот.
'''


def convertTemperature(temp, c):
    if c == 'f':
        return temp * 1.8 + 32
    elif c == 'c':
        return (temp - 32) / 1.8
    else:
        return "введите 'f' чтобы перевести в Фаренгейт или 'c' чтобы перевести в Цельсия"


print(convertTemperature(10, 'f'))
print(convertTemperature(50, 'c'))
print(convertTemperature(50, 'asd'))
