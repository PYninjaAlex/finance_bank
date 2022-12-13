import sqlite3 as sq

with sq.connect('users.db') as con:
    cur = con.cursor()
    cur.execute('DROP TABLE IF EXISTS users')
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
    cur.execute('''INSERT INTO users (name, sex, age, mail, job, company, username, adress)
     VALUES ("user_1", "F", 12, "skyportsoul@mail.ru", "programmer", "Yandex", "PYninjaAlex", "Krasnormeyskay str." )''')
