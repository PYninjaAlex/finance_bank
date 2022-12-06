import json

client_info = {}

def load():
    global client_info
    with open('client_info.json', 'r', encoding='utf-8') as json_file:
        client_info = json.load(json_file)

def save():
    with open('client_info.json', 'w', encoding='utf-8') as outfile:
        json.dump(client_info, outfile)


if __name__ == '__main__':
    command = ""
    while command != '10':
        print('Доступные действия: ')
        print('10 - выйти')

        command = input(' Выберите действие: ')

        if command == '10':
            print('До свидания.')
        else:
            print('Действие не распознано. Попробуйте ещё раз.')


