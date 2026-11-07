import sqlite3

conn = sqlite3.connect('practice.db')

cur = conn.cursor()

cur.execute(""" CREATE TABLE IF NOT EXISTS products (
                id INTEGER PRIMARY KEY,
                name TEXT,
                price INTEGER,
                quantity INTEGER
                )"""
            )
conn.commit()
conn.close()
