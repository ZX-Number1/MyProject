import sqlite3

conn = sqlite3.connect("test.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS users(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL,
    password TEXT NOT NULL
)
""")

cursor.execute("INSERT INTO users (username,password) VALUES(?,?)",("alice","123456"))
cursor.execute("INSERT INTO users (username,password) VALUES(?,?)",("bob","77486"))
cursor.execute("INSERT INTO users (username,password) VALUES(?,?)",("mary","69584"))
conn.commit() 

conn.close