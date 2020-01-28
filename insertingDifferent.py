import sqlite3 as lit


db = lit.connect('jobs.db')

with db:
    cursor = db.cursor()
    cursor.execute("INSERT INTO jobsList3(DESCRIPTION) VALUES('Description of job 1')")
    cursor.execute("INSERT INTO jobsList3(DESCRIPTION) VALUES('Description of job 2')")
    cursor.execute("INSERT INTO jobsList3(DESCRIPTION) VALUES('Description of job 3')")
    cursor.execute("INSERT INTO jobsList3(DESCRIPTION) VALUES('Description of job 4')")
    cursor.execute("INSERT INTO jobsList3(DESCRIPTION) VALUES('Description of job 5')")

    print("Data Inserted Successfully")
