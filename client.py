import json

client_info = {}

def load():
    global client_info
    with open('client_info.json', 'r', encoding='utf-8') as json_file:
        client_info = json.load(json_file)

def show_info():
    print("Информация о счетах")
    print("----------------------------------")
    print("Имя:", client_info['accounts'][0]['name'])
    print("Платёжная система:", client_info['accounts'][0]['system'])
    print("Номер:", client_info['accounts'][0]['number'])
    print("Тип:", client_info['accounts'][0]['type'])
    print("Баланс:", client_info['accounts'][0]['balance'])
    print("Срок действия до", client_info['accounts'][0]['validity period'])
    print("----------------------------------")
    print("Имя:", client_info['accounts'][1]['name'])
    print("Платёжная система:", client_info['accounts'][1]['system'])
    print("Номер:", client_info['accounts'][1]['number'])
    print("Тип:", client_info['accounts'][1]['type'])
    print("Баланс:", client_info['accounts'][1]['balance'])
    print("Срок действия до", client_info['accounts'][1]['validity period'])
    print("----------------------------------")

load()
show_info()