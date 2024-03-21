# TODO: Feature 5
import pytest
from app import app
from src.repositories.movie_repository import get_movie_repository

@pytest.fixture(scope='module')
def test_app():
    # Setup the Flask test client
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

@pytest.fixture(scope='module')
def new_movie():
    # Create a new movie for testing purposes
    movie_repository = get_movie_repository()
    movie = movie_repository.create_movie("Test Movie", "Test Director", 5)
    yield movie
    # Teardown - Delete the movie after test is done
    movie_repository.delete_movie(movie.movie_id)

def test_edit_movie_page(test_app, new_movie):
    # Test GET request for edit page
    response = test_app.get(f'/movies/{new_movie.movie_id}/edit')
    assert response.status_code == 200
    assert b"Edit Movie" in response.data
    assert b'value="Test Movie"' in response.data  # Check form is pre-populated with movie details

    # Test POST request to update movie details
    updated_data = {
        'title': 'Updated Test Movie',
        'director': 'Updated Test Director',
        'rating': '4'  # As string, because form data is sent as string
    }
    post_response = test_app.post(f'/movies/{new_movie.movie_id}', data=updated_data, follow_redirects=True)
    assert post_response.status_code == 200  # Check for a successful update response

    # Fetch the updated movie and verify its details have been updated
    updated_movie = get_movie_repository().get_movie_by_id(new_movie.movie_id)
    assert updated_movie.title == 'Updated Test Movie'
    assert updated_movie.director == 'Updated Test Director'
    assert updated_movie.rating == 4
