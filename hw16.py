'''
Написать программу, которая будет считывать из файла gps координаты,
и формировать текстовое описание объекта и ссылку на google maps.
Пример:

Input data: 60,01';30,19'
Output data:
Location: Теремок, Енотаевская улица, Удельная, округ Светлановское, Выборгский район,
 Санкт-Петербург, Северо-Западный федеральный округ, 194017, РФ
Goggle Maps URL: https://www.google.com/maps/search/?api=1&query=60.016666666666666,30.322

'''
from opencage.geocoder import OpenCageGeocode


key = '2ead87ca7a984517ba94f2b73a70edc5'
geocoder = OpenCageGeocode(key)
listGps = []
with open("hw16.txt",'r') as file:
    listGps = file.readlines()
for i in listGps:
    try:
        latlng = i.split(', ')
        results = geocoder.reverse_geocode(latlng[0], latlng[1])
    except:
        print("Не верно введённые данные")
        break
    print("Input data: ", i.strip('\n'))
    print("Output data: ")
    print("Location: ", results[0]['formatted'])
    print("Goggle Maps URL: https://www.google.com/maps/search/?api=1&query=" + latlng[0] + ',' + latlng[1])




