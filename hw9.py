from functools import reduce

def problem6():
    return ((sum([j for j in range(101)]))**2 - (sum([i*i for i in range(101)])))

def problem9():
    return ([(a * b * (1000-(a+b))) for a in range(500) for b in range(a) if a**2 + b**2 == (1000-(a+b))**2][0])

def problem40():
    '''
    с увеличением числа, количество цифр в нём увеличивается
так от 0 до 9 - 10 цифр (по 1 цифре на число)
от 10 до 99 - 90 чисел - 180 цифр (по 2 цифры на число)
от 100 до 999 - 900 чисел - 2.700 цифр (по 3 цифры на число)
так за 5-ти значное число набирается 488.890 цифр,
чтобы набрать ещё 511.110 нужно перебрать 85.185 6-ти значных чисел
    '''
    s = str(''.join([str(i) for i in range(185186)]))
    return (reduce(lambda a, b: int(a) * int(b), [s[10 ** i] for i in range(7)]))


def problem48():
    return (str(sum(i**i for i in range(1,1001)))[-10:])

print(f"Problem 6 - {problem6()}")
print(f"Problem 9 - {problem9()}")
print(f"Problem 40 - {problem40()}")
print(f"Problem 48 - {problem48()}")

