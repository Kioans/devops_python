'''
берём любое натуральное число n, если оно чётное,
то делим его на 2 если нечётное, то умножаем на 3
и прибавляем 1 (получаем 3n + 1) над полученным
числом выполняем те же самые действия, и так далее.
Гипотеза Коллатца заключается в том, что какое бы
начальное число n мы ни взяли, рано или поздно мы
получим единицу.
Задача
Вычислить число шагов для числа n, согласно гипотезе
Коллатца необходимых для достижения этим числом единицы.
'''
n = int(input())
f = 0
while n != 1:
     n = n // 2 if n % 2 == 0 else (n * 3 + 1)
     f +=1
print(f)