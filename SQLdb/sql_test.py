import sqlite3
from spisok import x

base = sqlite3.connect('new.db')
cur = base.cursor()
...
#text, integer, real, blob, null
...

# base.execute('CREATE TABLE IF NOT EXISTS {}(login PRIMARY KEY, password)'.format('data'))
# base.commit()
# создать таблицу
# ******************************************
# cur.execute('INSERT INTO data VALUES(?, ?)', ('jonny', '12345'))
# base.commit()
# cur.execute('INSERT INTO data VALUES(?, ?)', ('billy', '987875'))
# base.commit() # записи по строчно
# **************************************************
# cur.executemany('INSERT INTO data VALUES(?, ?)', (x))
# base.commit()
# запись массивом из файла
# *************************************************
# r = cur.execute('SELECT * FROM data').fetchall()
# получить все из таблицы

# r = cur.execute('SELECT login FROM data').fetchall()
# r = cur.execute('SELECT password FROM data').fetchall()
# получить все из столбца

# r = cur.execute('SELECT password FROM data WHERE login == ?', ('1')).fetchone()
# получить значение строки
# print(r)
# *********************************************************
# cur.execute('UPDATE data SET password == ? WHERE login == ?', ('1451361bghjsd', 'billy'))
# обновить пароль одной строки

# cur.execute('UPDATE data SET password == ? WHERE password == ?', ('1451361bghjsd', 'password'))
# обновить пароль несколько строк

# cur.execute('DELETE FROM data')
# удалить значение всей таблицы очистить

# cur.execute('DELETE FROM data WHERE login == ?', ('billy'))
# удалить строку

base.execute('DROP TABLE IF EXISTS data')
# удалить таблицу
base.commit()
base.close()