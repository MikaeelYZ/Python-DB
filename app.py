import sqlite3
from flask import Flask, render_template, request, url_for, flash, redirect
from werkzeug.exceptions import abort


def get_db_connection():
    conn = sqlite3.connect('filmflix.db')
    conn.row_factory = sqlite3.Row
    return conn

def get_post(post_id):
    conn = get_db_connection()
    post = conn.execute('SELECT * FROM tblFilms WHERE filmid = ?',
                        (post_id,)).fetchone()
    conn.close()
    if post is None:
        abort(404)
    return post

app = Flask(__name__)
app.config['SECRET_KEY']= 'thisisasecretkey'

@app.route('/')
def index():
    conn = get_db_connection()
    posts = conn.execute('SELECT * FROM tblFilms').fetchall()
    conn.close()
    return render_template('index.html', posts=posts)

@app.route('/<int:post_id>')
def post(post_id):
    post = get_post(post_id)
    return render_template('post.html', post=post)

@app.route('/create', methods=('GET', 'POST'))
def create():
    if request.method == 'POST':
        title = request.form['title']
        yearReleased = request.form['yearReleased']
        genre = request.form['genre']
        duration = request.form['duration']
        rating = request.form['rating']

        if not title:
            flash('Title is Required')
        elif not yearReleased:
            flash('Release Year is Required')
        elif not genre:
            flash('Genre is Required')
        elif not duration:
            flash('Duration is Required')
        elif not rating:
            flash('Film Rating is Required')
        else:
            conn = get_db_connection()
            conn.execute('INSERT INTO tblFilms (title, yearReleased, rating, duration, genre) VALUES (?, ?, ?, ?, ?)',
                         (title, yearReleased, rating, duration, genre))
            conn.commit()
            conn.close()
            return redirect(url_for('index'))

    return render_template('create.html')

@app.route('/<int:id>/edit', methods=('GET', 'POST'))
def edit(id):
    post = get_post(id)

    if request.method == 'POST':
        title = request.form['title']
        yearReleased = request.form['yearReleased']
        genre = request.form['genre']
        duration = request.form['duration']
        rating = request.form['rating']

        if not title:
            flash('Title is Required')
        elif not yearReleased:
            flash('Release Year is Required')
        elif not genre:
            flash('Genre is Required')
        elif not duration:
            flash('Duration is Required')
        elif not rating:
            flash('Film Rating is Required')
        else:
            conn = get_db_connection()
            conn.execute('UPDATE tblFilms SET title = ?, yearReleased = ?, genre = ?, duration = ?, rating = ?'
                         ' WHERE filmid = ?',
                         (title, yearReleased, rating, duration, genre, id))
            conn.commit()
            conn.close()
            return redirect(url_for('index'))

    return render_template('edit.html', post=post)

@app.route('/<int:id>/delete', methods=('POST',))
def delete(id):
    post = get_post(id)
    conn = get_db_connection()
    conn.execute('DELETE FROM tblFilms WHERE filmid = ?', (id,))
    conn.commit()
    conn.close()
    flash('"{}" was successfully deleted!'.format(post['title']))
    return redirect(url_for('index'))