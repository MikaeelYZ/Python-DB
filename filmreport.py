#creating subroutines for different filter conditions

from connect import *

def year():
    filmYear = input("Enter Year of Release: ")
    cursor.execute(f"SELECT * FROM tblFilms WHERE yearReleased = '{filmYear}'")

    row = cursor.fetchall()

    for aFilm in row:
        print(aFilm)

def rating():
    filmRating = input("Enter Film Rating: ")
    cursor.execute(f"SELECT * FROM tblFilms WHERE rating = '{filmRating}'")

    row = cursor.fetchall()

    for aFilm in row:
        print(aFilm)

def duration():
    filmDuration = input("Enter Duration of Film: ")
    cursor.execute(f"SELECT * FROM tblFilms WHERE duration = '{filmDuration}'")

    row = cursor.fetchall()

    for aFilm in row:
        print(aFilm)

def genre():
    filmGenre = input("Enter Genre of Film: ")
    cursor.execute(f"SELECT * FROM tblFilms WHERE genre = '{filmGenre}'")

    row = cursor.fetchall()

    for aFilm in row:
        print(aFilm)

if __name__ == "__main__":
    year()
    rating()
    duration()
    genre()
    