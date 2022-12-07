import json

client_info = {}

def load():
    global client_info
    with open('client_info.json', 'r', encoding='utf-8') as json_file:
        client_info = json.load(json_file)

def show_info():
    print("Информация о счетах")
    print("----------------------------------")
    for accounts in client_info['accounts']:
        print("Имя:", accounts['name'])
        print("Платёжная система:", accounts['system'])
        print("Номер:", accounts['number'])
        print("Тип:", accounts['type'])
        print("Баланс:", accounts['balance'])
        print("Срок действия до", accounts['validity period'])
        print("----------------------------------")

load()
show_info()