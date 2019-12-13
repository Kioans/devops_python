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

'''
a = input("Pirnt number (input) ")
b = raw_input("Print number (raw_input) ")

print(type(a))
print(type(b))
print(a+a)
print(b+b)

