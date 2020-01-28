import sqlite3 as lit


def main():
    try:
        db = lit.connect('jobs.db')
        cursor = db.cursor()

        # table_query = "CREATE TABLE jobsList (jobId INT PRIMARY KEY, description TEXT NOT NULL)"
        table_query = 'CREATE TABLE jobsList3(jobId INTEGER PRIMARY KEY AUTOINCREMENT, DESCRIPTION TEXT NOT NULL)'

        cursor.execute(table_query)
        print("Table created successfully")

    except:
        print("Failed to make table")

    finally:
        db.close()


if __name__ == "__main__":
    main()

