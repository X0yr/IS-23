import sqlite3 as sq
from data_user import user_ifo

with sq.connect('user.db') as con:
     cur = con.cursor()
with sq.connect('games.db') as cam:
     cir = cam.cursor()
cur.execute("DROP TABLE IF EXISTS users")
cur.execute("""CREATE TABLE IF NOT EXISTS users (
      id INTEGER PRIMARY KEY AUTOINCREMENT,
      sex INTEGER,
      name TEXT NOT NULL,
      level INTEGER,
      score INTEGER
     )""")

cir.execute("""CREATE TABLE IF NOT EXISTS games (
      id INTEGER PRIMARY KEY AUTOINCREMENT,
      user_id INTEGER,
      score INTEGER,
      time INTEGER
     )""")
#cir.execute("SELECT * FROM games WHERE user_id = 1")
#cir.execute("SELECT * FROM games WHERE score < 1000 AND user_id = 1")
#cir.execute("SELECT * FROM games WHERE score > 500 AND id BETWEEN 18 AND 21")
#cir.execute("SELECT * FROM games WHERE time >= 1559568764 AND id > 17")
#cir.execute("SELECT * FROM games WHERE user_id = 1 AND score > 1500 OR time > 1559471132")
#cir.execute("UPDATE games SET user_id = 2 WHERE id>20")
#cir.execute("UPDATE games SET time = 1559560000 WHERE id>19")
cir.execute("DELETE FROM games WHERE score < 100")
for resolt in cir:
     print(resolt)

#con.execute("INSERT INTO users VALUES(3, 1, 'Маия', 1, 0)")
#cir.execute("INSERT INTO games VALUES(22,1,1259,1559627528)")

cam.commit()
con.commit()