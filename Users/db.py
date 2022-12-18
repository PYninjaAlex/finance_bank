import random
import sqlite3 as sq
from faker import Faker

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


with sq.connect('users.db') as con:
    cur = con.cursor()
    # drop_table()
    # create_table()
    # add()
    # new_table()

cur.execute('''
    SELECT name, sex, age FROM users 
    WHERE sex = "M" 
    ORDER BY age DESC 
    LIMIT 5 OFFSET 10
''')

for result in cur:
    print(result)