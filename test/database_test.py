import sqlite3

connection = sqlite3.connect("laprender.db")
c = connection.cursor()

c.execute('''
    CREATE TABLE IF NOT EXISTS sessions
    (
    id INTEGER PRIMARY KEY,
    date TEXT NOT NULL,
    duration INTEGER NOT NULL
    )
''')
connection.commit()

c.execute("insert into sessions (date, duration) values ('20-10-26', 300)")
connection.commit()

result = c.execute("select * from sessions where date='20-10-26'")
print(result.fetchall())

c.close()