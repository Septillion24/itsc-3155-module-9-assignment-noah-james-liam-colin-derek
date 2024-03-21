from src.repositories.movie_repository import get_movie_repository
from app import app

def test_get_all_movies():
    movies = get_movie_repository()
    movies.clear_db()
    movies.create_movie("Movie", "Dir", 5)
    movies2 = movies.get_all_movies()

    assert list(movies2.values())[0].title == "Movie"
    assert list(movies2.values())[0].director == "Dir"
    assert list(movies2.values())[0].rating == 5
    
    movies.clear_db()
    
    