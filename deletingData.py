import sqlite3 as lit

db = lit.connect('jobs.db')

with db:
    jobId = 4

    cursor = db.cursor()
    cursor.execute("DELETE FROM jobsList WHERE jobId = ? ", (jobId,))

    db.commit()
    print("Data deleted successfully")