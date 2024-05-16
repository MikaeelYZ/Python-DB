from connect import *

def read():
    try:
        cursor.execute("SELECT * FROM tblFilms")

        row = cursor.fetchall()

        for aTitle in row:
            print(aTitle)

    except sql.OperationalError as e:
        print(f"Movie Title not found: {e}")

if __name__ == "__main__":
    read()