import sqlite3

conn = sqlite3.connect('music.sqlite')
cur = conn.cursor()

cur.execute('INSERT INTO Artist (id, name, eyes) VALUES (42, "Frank Sinatra", "blue");')


cur.execute('INSERT INTO Track (title, plays, artist_id) VALUES ("My Way", 15, 42);')
cur.execute('INSERT INTO Track (title, plays, artist_id) VALUES ("New York", 25, 42);')
conn.commit()

print('Track:')
# cur.execute('SELECT title, plays, artist_id FROM Track')
cur.execute('SELECT title, plays, name, eyes FROM Track JOIN Artist ON Track.artist_id = Artist.id;')
for row in cur:
     print(row)

cur.execute('DELETE FROM Track WHERE plays < 100')
cur.execute('DELETE FROM Artist')
conn.commit()

cur.close()
