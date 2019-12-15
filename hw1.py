from pip._vendor.distlib.compat import raw_input

print(bool(True)) #True
print(bool(0)) #False
print(bool(1)) #True
print(bool(2)) #True
print(bool(5)) #True
print(bool("hello")) #True
print(bool("T")) #True
print(bool("False")) #True
print(bool([])) #True
print("------")
print((False == 123)) #False
print((False == 0)) #True
print((True == 1)) #True
print((True == "hi")) #False
print(True is 1) #False

'''
raw_input() возвращает строковые значения
input() преобразует тип данных 
в python 3.x raw_input() переименован в input() и выполняет те же функции 
'''
a = input("Pirnt number (input) ")
b = raw_input("Print number (raw_input) ")
print(type(eval(input('Text here')))) #int
print(type(a)) #str
print(type(b)) #str

print(a+a)
print(b+b)

'''
в python3 оператор print был сделан функцией для удобства, при сложных синтаксических конструкциях
в функции print() легче ориентироваться 
 
'''
