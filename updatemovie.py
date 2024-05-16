from connect import *

def update():
    idField = input("Enter the ID of the movie to be updated: ")

    fieldName = input("Enter the field to be updated (Title, Year Released, Rating, Duration, Genre): ")

    newValue = input(f"Enter New Value for {fieldName}: ")
    print(newValue)


    try:
        cursor.execute(f"UPDATE tblFilms SET {fieldName} = '{newValue}' WHERE filmID = {idField}")
        conn.commit()
        print(f"Movie {idField} has been updated")

    except sql.OperationalError as e:
        conn.rollback()
        print(f"Movie not updated: {e}")

if __name__ == "__main__":
    update()