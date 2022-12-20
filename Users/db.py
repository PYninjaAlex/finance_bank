import random
import sqlite3 as sq
from faker import Faker

cur = None
def drop_table():
    cur.execute('DROP TABLE IF EXISTS users')


def create_table():
    cur.execute('''CREATE TABLE IF NOT EXISTS users(
        name TEXT NOT NULL,
        sex TEXT,
        age INTEGER NOT NULL DEFAULT 1,
        mail TEXT,
        job TEXT,
        company TEXT,
        username TEXT,
        adress TEXT
        )''')

def new_table():
    cur.execute('DROP TABLE IF EXISTS id')
    cur.execute('''CREATE TABLE IF NOT EXISTS id(
        user_1_id TEXT NOT NULL
        )''')
    cur.execute('INSERT INTO id (user_1_id) VALUES (532131) ')

def add():
    for i in range(100):
        user = fake.profile()
        cur.execute(f''' 
                INSERT INTO users VALUES(
                "{user["name"]}",
                "{user["sex"]}",
                {random.randint(10, 35)},
                "{user["mail"]}",
                "{user["job"]}",
                "{user["company"]}",
                "{user["username"]}",
                "{user["address"]}"
                )    
            ''')

fake = Faker(locale="ru_RU")

def update_student():
    cur.execute('''
    UPDATE users 
    SET job = 'student' 
    WHERE age 
    BETWEEN 16 AND 21
''')


def delete_user_name():
    cur.execute('''
    DELETE FROM users
    WHERE name = 'Пелагея Ивановна Суворова'
''')


def set_req():
    cur.execute('''
    UPDATE users 
    SET age = age + 5
    WHERE job = 'student'
''')


def first_select():
    print('First select =>\n')
    cur.execute('''
    SELECT name, sex, age, job FROM users
    WHERE sex = "M" and
    age BETWEEN 10 AND 30
    ORDER BY age
''')
    for result in cur:
        print(f'\t{result}')


def second_select():
    print('\nSecond select =>\n')
    cur.execute('''
    SELECT rowid, name FROM users
    WHERE name BETWEEN 'Александр Андреевич Живагин'
    AND 'Пелагея Ивановна Суворова'
    ORDER BY name
''')
    for result in cur:
        print(f'\t{result}')




with sq.connect('users.db') as con:
    cur = con.cursor()
    update_student()
    delete_user_name()
    set_req()
    first_select()
    second_select()
    # drop_table()
    # create_table()
    # add()
    # new_table()