from flask import Flask, abort, redirect, render_template, request
import sys

from src.models.movie import Movie
from src.repositories.movie_repository import get_movie_repository

app = Flask(__name__)

# Get the movie repository singleton to use throughout the application
movie_repository = get_movie_repository()


@app.get('/')
def index():
    return render_template('index.html')


@app.get('/movies')
def list_all_movies():
    # TODO: Feature 1
    return render_template('list_all_movies.html', list_movies_active=True)


@app.get('/movies/new')
def create_movies_form():
    return render_template('create_movies_form.html', create_rating_active=True)


@app.post('/movies')
def create_movie():
    # TODO: Feature 2
    # After creating the movie in the database, we redirect to the list all movies page
    return redirect('/movies')


@app.get('/movies/search')
def search_movies():
    # TODO: Feature 3
    return render_template('search_movies.html', search_active=True)

@app.post('/movies/searched')
def searched_movies():
    title = request.form.get('movie')
    title1 = "Ferris Bueller's Day Off"
    title2 = "The Avenger's"
    title3 = "Frozen"
    print(title, file=sys.stderr)
    if title1 == title:
        movie = Movie(456, "Ferris Bueller's Day Off", 'John Hguhes', 4)
    elif title2 == title:
        movie = Movie(789, "The Avenger's", 'Joss Whedon', 5)
    elif title3 == title:
        movie = Movie(147, 'Frozen', 'Jennifer Lee', 2)
    else:
        movie = Movie(123, 'Star Wars', 'George Lucas', 4)
    return render_template('searched.html', movie=movie)


@app.get('/movies/<int:movie_id>')
def get_single_movie(movie_id: int):
    # TODO: Feature 4
    
    # generate a fake movie for testing
    movie = Movie(123, 'Star Wars', 'George Lucas', 4)
    
    # movie = movie_repository.get_movie_by_id(movie_id)
    
    if movie == None:
        abort(404)
    return render_template('get_single_movie.html',movie=movie)


@app.get('/movies/<int:movie_id>/edit')
def get_edit_movies_page(movie_id: int):
    return render_template('edit_movies_form.html')


@app.post('/movies/<int:movie_id>')
def update_movie(movie_id: int):
    # TODO: Feature 5
    # After updating the movie in the database, we redirect back to that single movie page
    return redirect(f'/movies/{movie_id}')


@app.post('/movies/<int:movie_id>/delete')
def delete_movie(movie_id: int):
    # TODO: Feature 6
    pass
