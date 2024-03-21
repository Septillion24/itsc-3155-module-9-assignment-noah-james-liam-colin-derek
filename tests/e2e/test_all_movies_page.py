from src.repositories.movie_repository import get_movie_repository
from app import app

def test_all_movies_blank():
    test_app = app.test_client()
    response = test_app.get('/movies')
    #checks to see if /movies can be accessed
    assert 200 == response.status_code

def test_all_movies_no_movies():
    movies = get_movie_repository()
    movies.clear_db()
    movies.create_movie("Movie", "Dir", 5)

    test_app = app.test_client()
    response = test_app.get('/movies')
    #checks to see if a table element containing the number 5, which should be the only rating in the table, exists
    assert b"<td>5</td>" in response.data




