from fastapi import FastAPI, HTTPException
import mysql.connector as mysql
from movie import Movie

mydb = mysql.connect(
    host='localhost', user='root', password="", database="movies")

mycursor = mydb.cursor()
app = FastAPI()


movies = [{}, {
    'title': 'batman',
    'year': 2021,
    'length': 180
}, {
    'title': 'Avatar 2',
    'year': 2022,
    'length': 180
}
]


@app.get('/movies')
def get_movies():
    sql = 'SELECT * FROM movies_api'
    mycursor.execute(sql)
    movies = mycursor.fetchall()

    return movies

# GET BY ID


@app.get('/movies_by_id/{id}')
def get_movie(id: int):
    sql = 'SELECT * FROM movies_api WHERE id = %s '
    value = (id,)
    mycursor.execute(sql, value)
    movie = mycursor.fetchall()
    return movie
# GET BY TITLE


@app.get('/movies_by_title/{title}')
def get_movie_by_title(title: str):

    sql = 'SELECT * FROM movies_api WHERE title = %s'
    value = (title,)
    mycursor.execute(sql, value)
    movie = mycursor.fetchall()
    if len(movie) == 0:
        raise HTTPException(status_code=500, detail='Movie not found!')
    return movie[0]

# Delete


@app.delete('/movies/{id}')
def delete_movie(id: int):
    sql = 'DELETE FROM movies_api WHERE id = %s'
    value = (id,)
    mycursor.execute(sql, value)
    movie = mycursor.fetchall()

    return {'message': 'movie has been deleted'}

# insert


@app.post('/movie')
def add_movie(movie: Movie):
    sql = 'INSERT INTO movies_api(title,year,detailes) VALUES (%s,%s,%s)'
    value = (movie.title, movie.year, movie.detailes)
    mycursor.execute(sql, value)
    mydb.commit()
    return movie

# update


@app.post('/update_movie')
def update_movie(movie: Movie, id: int):

    sql = 'UPDATE movies_api SET title = %s,year = %s,detailes= %s WHERE ID = %s'
    values = (movie.title, movie.year, movie.detailes, id)
    mycursor.execute(sql, values)
    mydb.commit()
    return movie
