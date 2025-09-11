import sqlite3

conn =sqlite3.connect("test.db")
cursor = conn.cursor()

cursor.execute("SELECT username, password FROM users")

for row in cursor.fetchall():
    print(row)

conn.close()