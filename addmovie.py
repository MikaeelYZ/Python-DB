from connect import *

def insertMovie():
    movie = []

    title = input("Enter Name of Film: ")
    year = input("Enter Year of Release: ")
    rating = input("Enter Film Rating: ")
    duration = input("Enter Duration of Film: ")
    genre = input("Enter Genre of Film: ")

    movie.append(title)
    movie.append(year)
    movie.append(rating)
    movie.append(duration)
    movie.append(genre)

    print(movie)

    try:
        cursor.execute("INSERT INTO tblFilms (title, yearReleased, rating, duration, genre) VALUES (?,?,?,?,?)", movie)
        conn.commit()
        print(f"{title} added to table of films")

    except sql.OperationalError as e:
        conn.rollback()
        print(f"Movie not added: {e}")

if __name__ == "__main__":
    insertMovie()