import sqlite3

conn = sqlite3.connect('myquotes.db')
curr = conn.cursor()

# curr.execute("""create table quotes_tb(
#                 title text,
#                 author text
#                 )""")

curr.execute("""insert into quotes_tb values('Python is awesome','DA')""")
conn.commit()
conn.close()