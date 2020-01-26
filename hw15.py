import ipaddress

class router:
    def __init__(self):
        self.list_ip_adress = []  # лист в котором хранятся ip адреса
        self.list_ip_routers = []  # лист в котором ранятся листы с двумя элементами
        # ip адрес интерфейса и ip адрес сети

    def add_ip_adress(self, ip_adres):
        try:
            if ip_adres not in self.list_ip_adress:
                self.list_ip_adress.append(ipaddress.ip_interface(ip_adres))
                return f'ip адрес {ip_adres} успешно добавлен'
            else:
                return 'Введённый {ip_adres} ip адрес уже существует'
        except:
            return 'Не корректно введён ip адрес'

    def del_ip_adress(self, ip_adres):
        ip_adres = ipaddress.ip_interface(ip_adres)
        try:
            self.list_ip_adress.remove(ip_adres)
            print(f'ip адресс {ip_adres} успешно удалён')
        except:
            print('Не корректно введён ip адрес')

    def print_ip_adress(self):
        print("Список ip адресов")
        for i in self.list_ip_adress:
            print(i)

    def add_ip_route(self, ip_adres, ip_gateway):
        try:
            ip_gateway = ipaddress.ip_address(ip_gateway)
            ip_adres = ipaddress.ip_network(ip_adres)
        except ValueError:
            return 'Введите корректный ip адрес'
        if (not self.in_list_ip_adress(ip_gateway)) and (not self.in_list_ip_routers(ip_gateway)):
            return 'Маршрут до шлюза отсутствует'
        if [ip_gateway, ip_adres] in self.list_ip_routers:
            return 'Данный маршрут уже присутствует в таблице'
        self.list_ip_routers.append([ip_gateway, ip_adres])
        return f'Маршрут до  {ip_adres}, через {ip_gateway} успешно добавлен'

    def del_ip_routes(self, ip_adres):
        del_well = False
        try:
            ip_adres = ipaddress.ip_network(ip_adres)
        except ValueError:
            return 'Введите корректный ip адрес интерфейса'
        for route in self.list_ip_routers:
            if route[1] == ip_adres:
                self.list_ip_routers.remove(route)
                self.del_ip_routes(route[1])
                del_well = True
            if route[0] in ip_adres:  # удалив шлюз теряются доступные через него ip адреса, их тоже нужно почистить
                self.del_ip_routes(route[1])
        if del_well:
            print("Удаление шлюза выполнено успешно")
        return "Не корректно введён ip router"

    def print_ip_routes(self):
        print("Список маршрутов")
        for i in self.list_ip_routers:
            print(f'Адрес шлюза - {i[0]} , сеть - {i[1]}')

    # проверям принадлежность ip адреса одной из сетей в list_ip_adress
    def in_list_ip_adress(self, ip_adres):
        for address in self.list_ip_adress:
            if ip_adres in address.network:
                return True
        return False

    # проверяем наличие маршрута до сети
    def in_list_ip_routers(self, ipGateway):
        for routers in self.list_ip_routers:
            if ipGateway in routers[1]:
                return True
        return False

    def info_router(self):
        print("Информация о маршрутах и ip адресах")
        self.print_ip_adress()
        self.print_ip_routes()
        print(f'Итого - {len(self.list_ip_adress)} интерфейсов и {len(self.list_ip_routers)} маршрутов')


myRouter = router()
print(myRouter.add_ip_adress('192.168.5.14/24'))
print(myRouter.add_ip_adress('192.169.5.2/24'))
print(myRouter.add_ip_route('172.16.0.0/16', '192.168.5.1'))
print(myRouter.add_ip_route('172.24.0.0/16', '192.168.8.1'))
print(myRouter.add_ip_route('172.24.0.0/16', '172.16.8.1'))
print(myRouter.add_ip_route('173.16.0.0/16', '192.169.5.1'))
print(myRouter.add_ip_route('173.24.0.0/16', '192.169.8.1'))
print(myRouter.add_ip_route('173.24.0.0/16', '173.16.8.1'))

myRouter.del_ip_routes('172.16.8.1')
myRouter.del_ip_routes('192.169.5.1')  # удаляет сразу две сети 173.16.0.0/16 , 173.24.0.0/16
# так как маршрут до 173.24.0.0/16 лежи в сети 173.16.0.0/16, шлюз до которой 192.169.5.1
# myRouter.del_ip_adress('192.169.5.2/24')
myRouter.info_router()


