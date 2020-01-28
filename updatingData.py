import sqlite3 as lit

db = lit.connect('jobs.db')

with db:
    newDescription = "updated description"
    jobId = 5

    cursor = db.cursor()
    cursor.execute('UPDATE jobsList SET description = ? WHERE jobId = ? ', (newDescription, jobId))
    db.commit()
    print("Data updated successfully")

