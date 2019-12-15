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
raw_input() возвращает строковые значения
input() преобразует тип данных 
в python 3.x raw_input() переименован в input() и выполняет те же функции 
'''
a = input("Input ")
b = raw_input("Raw_input   ")
print(type(eval(input('Text here '))))  # int
print(type(a))  # str
print(type(b))  # str

print(a + a)
print(b + b)

'''
в python3 оператор print был сделан функцией для удобства, при сложных синтаксических конструкциях
в функции print() легче ориентироваться 
 
'''
print(a , b, sep=' separator ', end='\n', file=None)