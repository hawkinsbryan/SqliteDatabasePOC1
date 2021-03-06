import sqlite3 as lit

db = lit.connect('jobs.db')
db.text_factory = str  # removes the u in the fetchall

with db:
    cursor = db.cursor()
    select_query = "SELECT * FROM jobsList"
    cursor.execute(select_query)

    rows = cursor.fetchall()

    for data in rows:
        print(data)