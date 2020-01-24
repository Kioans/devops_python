'''
Написать функцию Фиббоначи fib(n), которая вычисляет
элементы последовательности Фиббоначи:
1 1 2 3 5 8 13 21 34 55 .......
'''


def fib(n):
    a = 0
    b = 1
    s = []
    for i in range(n):
        a, b = b + a, a
        s.append(a)
    return s


n = int(input())
print(fib(n))