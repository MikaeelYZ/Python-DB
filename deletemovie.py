from connect import *

def delete():
    idField = input("Enter FilmID to delete: ")

    try:
        cursor.execute(f"DELETE FROM tblFilms WHERE filmID = {idField}")
        conn.commit()
        print(f"Movie {idField} has been deleted")

    except sql.OperationalError as e:
        conn.rollback()
        print(f"Movie not found in Database: {e}")

if __name__ == "__main__":
    delete()