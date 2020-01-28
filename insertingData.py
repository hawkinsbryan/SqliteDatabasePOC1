import sqlite3 as lit

jobsList = (
    ('Description of job 3',),
    ('Description of job 4',),
    ('Description of job 5',),
    ('Description of job 6',)

)

db = lit.connect('jobs.db')

with db:
    cursor = db.cursor()
    cursor.executemany('INSERT INTO jobsList VALUES (?,?)', jobsList)

    print("Data Inserted Successfully")
