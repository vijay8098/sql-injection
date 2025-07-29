import sqlite3

conn = sqlite3.connect('database.db')
cursor = conn.cursor()
cursor.execute('CREATE TABLE users (username TEXT, password TEXT)')
cursor.execute("INSERT INTO users VALUES ('admin', 'adminpass')")
cursor.execute("INSERT INTO users VALUES ('user', 'userpass')")
conn.commit()
conn.close()
