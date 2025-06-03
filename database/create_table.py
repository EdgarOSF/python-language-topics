import sqlite3

conn = sqlite3.connect('music.sqlite')

cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS Track')
cur.execute('CREATE TABLE Track (title TEXT, plays INTEGER, artist_id INTEGER);')

cur.execute('DROP TABLE IF EXISTS Artist')
cur.execute('CREATE TABLE Artist (id INTEGER, name TEXT, eyes TEXT);')

conn.close()

