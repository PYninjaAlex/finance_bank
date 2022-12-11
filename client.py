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


def predict():
    month = []
    sum_cancelletion = 0
    sum_income = 0
    for transaction in client_info['transactions']:
        if transaction["type"] == 'списание':
            sum_cancelletion += transaction['amount']
        elif transaction["type"] == 'зачисление':
            sum_income += transaction['amount']
        if transaction["date"] not in month:
            month.append(transaction["date"])

    print("Предполагаемые расходы в следующем месяце: ", sum_cancelletion / len(month))
    print("Предполагаемые доходы в следующем месяце: ", sum_income / len(month))

load()
show_info()
predict()