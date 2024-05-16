import sqlite3 as sql

try:
    with sql.connect("filmflix.db") as conn:
        cursor = conn.cursor()
        print("Database Formed")

except sql.OperationalError as e:
    print(f"Failed to connect with Database: {e}")