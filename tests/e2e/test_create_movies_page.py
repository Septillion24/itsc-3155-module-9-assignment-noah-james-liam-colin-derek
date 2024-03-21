from src.repositories.movie_repository import get_movie_repository
from app import app

def test_create_movie_with_empty_title(test_app):
    data={'movieName': '', 'directorName': 'Jarold', 'rating': 5}
    response = test_app.post('/movies', data=data)

    assert response.status_code == 400

    response_data = response.data.decode('utf-8')

    assert f'Invalid input: Movie name required' in response_data
