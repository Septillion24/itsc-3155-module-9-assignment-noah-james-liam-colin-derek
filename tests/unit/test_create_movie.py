from flask import app
from src.repositories.movie_repository import get_movie_repository

def test_create_movie():
    movie_repo = get_movie_repository()
    movie_repo.clear_db()
    movie_name = 'The Matrix'
    director_name = 'Jarold'
    rating = 5

    movie = movie_repo.create_movie(movie_name, director_name, rating)

    assert movie.title == movie_name
    assert movie.director == director_name
    assert movie.rating == rating
