import json
from faker import Faker
users_info = {}
fake = Faker(locale="ru_RU")

def load():
    global users_info
    with open('users_info.json', 'r', encoding='utf-8') as json_file:
        users_info = json.load(json_file)

def add():
    for i in range(100):
        users_info['Users'].append(fake.profile())
# print(fake.profile())
def save():
    with open('users_info.json', 'w', encoding='utf-8') as outfile:
        json.dump(users_info, outfile)

load()
add()
save()


