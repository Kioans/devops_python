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

def get_location(lat='X', lng='X'):
    key = '2ead87ca7a984517ba94f2b73a70edc5'
    file_gps = "hw16.txt"
    listGps = []
    geocoder = OpenCageGeocode(key)
    if lat != 'X' and lng != 'X':
        listGps.append(str(lat + ', ' + lng))
        results = geocoder.reverse_geocode(lat, lng)
        print_location(results)
    else:
        with open(file_gps,'r') as file:
            listGps = file.readlines()
        for i in listGps:
            try:
                latlng = i.split(', ')
                results = geocoder.reverse_geocode(latlng[0], latlng[1])
            except:
                print("Не верно введённые данные")
                break
            print_location(results)

def print_location(results):
    print("Input data: ", results[0]['geometry']['lat'], results[0]['geometry']['lng'])
    print("Output data: ")
    print("Location: ", results[0]['formatted'])
    lat = str(results[0]['geometry']['lat'])
    lng = str(results[0]['geometry']['lng'])
    print("Goggle Maps URL: https://www.google.com/maps/search/?api=1&query=" + lat + ',' + lng)


if __name__ == '__main__':
    get_location()
