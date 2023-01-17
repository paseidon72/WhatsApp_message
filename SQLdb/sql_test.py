import sqlite3
from spisok import x

base = sqlite3.connect('new.db')
cur = base.cursor()
...
#text, integer, real, blob, null
...

# base.execute('CREATE TABLE IF NOT EXISTS {}(login PRIMARY KEY, password)'.format('data'))
# base.commit()
#
# cur.execute('INSERT INTO data VALUES(?, ?)', ('jonny', '12345'))
# base.commit()
# cur.execute('INSERT INTO data VALUES(?, ?)', ('billy', '987875'))
# base.commit()
# cur.executemany('INSERT INTO data VALUES(?, ?)', (x))
# base.commit()
# r = cur.execute('SELECT * FROM data').fetchall()
# r = cur.execute('SELECT login FROM data').fetchall()
# r = cur.execute('SELECT password FROM data').fetchall()
# r = cur.execute('SELECT password FROM data WHERE login == ?', ('1')).fetchone()
# print(r)
# cur.execute('UPDATE data SET password == ? WHERE login == ?', ('1451361bghjsd', 'billy'))
# cur.execute('UPDATE data SET password == ? WHERE password == ?', ('1451361bghjsd', 'password'))
# cur.execute('DELETE FROM data')
# cur.execute('DELETE FROM data WHERE login == ?', ('billy'))
base.execute('DROP TABLE IF EXISTS data')
base.commit()
base.close()