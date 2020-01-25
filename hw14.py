'''
Создать сотрудника Mary, пользуясь классом
Employee и перенести его в другую программу,
используя модуль Pickle и файловую систему.
Узнать про + и - модуля Pickle.

'''
import pickle

class Employee:
    empCount = 0
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.empCount += 1
        self.empID = Employee.empCount

    def add_salary(self, delta=10000):
        self.salary = self.salary + delta

    def printEmployee(self):
        print(f"Employee name: {self.name} , salary: {self.salary}, ID: {self.empID}")


Mary = Employee("Mary", 50000)
Jhon = Employee("Jhon", 60000)
Mary.printEmployee()
Jhon.printEmployee()
with open("pickle","wb") as file:
    pickle.dump(Mary,file)

with open("pickle","rb") as file:
    Mary_from_file = pickle.load(file)

print(f"Mary's dump: {Mary_from_file}")
Mary_from_file.printEmployee()