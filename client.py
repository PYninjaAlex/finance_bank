import json

client_info = {}

def load():
    global client_info
    with open('client_info.json', 'r', encoding='utf-8') as json_file:
        client_info = json.load(json_file)

def show_info():
    i = 0
    l = len(client_info['accounts'])
    print("Информация о счетах")
    print("----------------------------------")
    for accounts in client_info['accounts']:
        print("Имя:", client_info['accounts'][i]['name'])
        print("Платёжная система:", client_info['accounts'][i]['system'])
        print("Номер:", client_info['accounts'][i]['number'])
        print("Тип:", client_info['accounts'][i]['type'])
        print("Баланс:", client_info['accounts'][i]['balance'])
        print("Срок действия до", client_info['accounts'][i]['validity period'])
        print("----------------------------------")

load()
show_info()