from pip._vendor.distlib.compat import raw_input

print("bool(True) -> ", bool(True))  # True
print("bool(False) -> ", bool(False))  # True
print("bool(0) -> ", bool(0))  # False
print("bool(1) -> ", bool(1))  # True
print("bool(2) ->", bool(2))  # True
print("bool(5) -> ", bool(5))  # True
print("bool('hello') -> ", bool("hello"))  # True
print("bool('T') -> ", bool("T"))  # True
print("bool('False') -> ", bool("False"))  # True
print("bool('True') -> ", bool("True"))  # True
print("bool([]) -> ", bool([]))  # True
print("------")
print("False == 123 -> ", False == 123)  # False
print("False == 0 -> ", False == 0)  # True
print("True == 1 -> ", True == 1)  # True
print("True == 'hi' -> ", True == "hi")  # False
print("True is 1 -> ", True is 1)  # False
print("True is 'True' -> ", True is 'True')
'''
Python 2.x
raw_input() читает данные из sys.stdin и преобразовывает в строку
    _____________________________________________________________________
    >>>  my_str = raw_input()  
    2+2
    >>> print(my_str) 
    2+2 
    _____________________________________________________________________
input() оценивает ввод в контексте выполнения ожидает корректного выражения
    >>> b = input()
    2+2
    >>> print(b)
    4
    
Python 3.x  
    eval(input()) вызывет input() из python 2.x
    _____________________________________________________________________
    >>> b = eval(input())
    2+2
    >>> print(b)
    4
    _____________________________________________________________________
в python 3.x raw_input() переименован в input() и выполняет те же функции
    _____________________________________________________________________
    >>> a=input()
    2+2
    >>> print(a)
    2+2 
    ______________________________________________________________________
'''
a = input("Input ")
b = raw_input("Raw_input   ")
print(type(eval(input('Text here '))))  # int
print(type(a))  # str
print(type(b))  # str

print(a + a)
print(b + b)

'''
в python3 оператор print был сделан функцией для удобства, при сложных 
синтаксических конструкциях в функции print() легче ориентироваться 
'''
print(a , b, sep=' separator ', end='\n', file=None)

'''
оператор print в python2
автоматически преобразует элементы в строки
автоматически вставляет пробелы между элементами
добавляет новую строку, если оператор не заканчивается запятой

______________________________________________________________

функция print() в python3
имеет следующую структуру:
def print(*args, sep=' ', end='\n', file=None)
автоматически преобразует элементы в строки
можно задать символ(ы) которые будут между элементами

теперь метод ptint() можно передавать в качестве параметра
раньше можно было использовать только как инструкцию

По умолчанию
между элементами вставляется пробел
в качестве параметра end используется ‘\n’
file — используется файл sys.stdout  
если нужно вывести в файл, в качестве аргумента указывется дескриптор 
таким образом синтаксис кода получается чище 
пример: 
>>>fid = open("text.txt", "a")
>>>print("abcdef", file=fid)'
'''