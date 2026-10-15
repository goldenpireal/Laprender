import sqlite3

def save_session(duration, date):
    conn = sqlite3.connect("laprender.db")
    c = conn.cursor()

    c.execute("""
                CREATE TABLE IF NOT EXISTS sessions
                (

                id INTEGER PRIMARY KEY,
                date TEXT NOT NULL,
                duration INTEGER NOT NULL
                
                )
                
                """)
    conn.commit()

    c.execute("""
                INSERT INTO sessions(duration, date) VALUES(?, ?)
                """,
              (duration, date))
    conn.commit()


    conn.close()

conn = sqlite3.connect("laprender.db")
c = conn.cursor()

result = c.execute("select * from sessions")
print(result.fetchall())

conn.close()