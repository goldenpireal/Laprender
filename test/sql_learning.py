import sqlite3

connection = sqlite3.connect("learning.db")

c = connection.cursor()

'''c.execute("""CREATE TABLE employees (

    first text,
    last text,
    pay integer

)""")'''

#c.execute("INSERT INTO employees VALUES ('Nt','ff',676767)")

c.execute("select * from employees where last='ff'")
print(c.fetchall())

connection.commit()

connection.close()