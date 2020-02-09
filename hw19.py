import socket

root_dns = {}
provider_dns = {}

dns = {}

while True:
    tmp_list = ()
    input_hostname = input("Введите назание сайта: ")
    try:
        response = socket.gethostbyname(input_hostname)
        if input_hostname not in dns:
            dns[input_hostname] = set()
        dns[input_hostname].add(response)
        print(f"IP адрес сайта {input_hostname}: {response}")
    except:
        print("Не возможно получить IP адрес")
