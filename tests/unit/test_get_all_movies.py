from src.repositories.movie_repository import get_movie_repository
from app import app

def test_movie_add():
    movies = get_movie_repository()
    movies.clear_db()
    movies.create_movie("Movie", "Dir", 5)
    assert movies.get_movie_by_title("Movie").director == "Dir"
    movies.clear_db()