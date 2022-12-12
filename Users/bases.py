import json
from faker import Faker
users_info = {}
fake = Faker(locale="ru_RU")

def load():
    global users_info
    with open('users_info_out.json', 'r', encoding='utf-8') as json_file:
        users_info = json.load(json_file)

def add():
    for i in range(100):
        user = fake.profile()
        del user['current_location']
        del user['birthdate']
        users_info['Users'].append(user)

def save():
    with open('users_info_out.json', 'w', encoding='utf-8') as outfile:
        json.dump(users_info, outfile)

load()
add()
save()


