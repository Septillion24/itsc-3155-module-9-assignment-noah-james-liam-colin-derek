from flask import Flask, abort, redirect, render_template, request

from src.repositories.movie_repository import get_movie_repository

app = Flask(__name__)

# Get the movie repository singleton to use throughout the application
movie_repository = get_movie_repository()


@app.get('/')
def index():
    return render_template('index.html')


@app.get('/movies')
def list_all_movies():
    movies = movie_repository.get_all_movies()

    return render_template('list_all_movies.html', movies = movies, list_movies_active=True)


@app.get('/movies/new')
def create_movies_form():
    return render_template('create_movies_form.html', create_rating_active=True)


@app.post('/movies')
def create_movie():
    # After creating the movie in the database, we redirect to the list all movies page
    if request.form.get('movieName').strip() == '':
        abort(400, "Invalid input: Movie name required")
    else:
        movieName = request.form.get('movieName')
    if request.form.get('directorName').strip() == '':
        abort(400, "Invalid input: Director name required")
    else:
        movieDirector = request.form.get('directorName')
    if request.form.get('rating') in ['1', '2', '3', '4', '5']:
        movieRating = request.form.get('rating')
    else:
        abort(400, "Invalid input: Rating required")
    
    movie = movie_repository.create_movie(movieName, movieDirector, movieRating)

    return redirect('/movies')


@app.get('/movies/search')
def search_movies():
    return render_template('search_movies.html', search_active=True)

@app.post('/movies/searched')
def searched_movies():
    title = request.form.get('movie')
    movie = None
    all_movies = movie_repository.get_all_movies()
    for x in all_movies.values():
        if x.title == title:
            movie = x
    if movie == None:
        abort(404)
    return redirect("/movies/" + str(movie.movie_id), code=200)


@app.get('/movies/<int:movie_id>')
def get_single_movie(movie_id: int):
    
    movie = movie_repository.get_movie_by_id(movie_id)
    
    if movie == None:
        abort(404)
    return render_template('get_single_movie.html',movie=movie)


@app.get('/movies/<int:movie_id>/edit')
def get_edit_movies_page(movie_id: int):
    movie = movie_repository.get_movie_by_id(movie_id)
    if movie == None:
        abort(404)
    return render_template('edit_movies_form.html',movie=movie,create_rating_active=True)


@app.post('/movies/<int:movie_id>')
def update_movie(movie_id: int):
    # After updating the movie in the database, we redirect back to that single movie page

    # Extracting Movie Data
    title = request.form['title']
    director = request.form['director']
    rating = int(request.form['rating'])

    # Attempt Update
    try:
        movie_repository.update_movie(movie_id, title, director, rating)
    except:
        abort(404)

    # Return to Movie Page
    return redirect(f'/movies/{movie_id}')

# we only have 5 guys (burger)
# @app.post('/movies/<int:movie_id>/delete')
# def delete_movie(movie_id: int):
#     # TODO: Feature 6
#     pass
