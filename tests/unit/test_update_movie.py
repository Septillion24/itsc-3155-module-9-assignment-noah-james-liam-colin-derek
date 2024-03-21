# TODO: Feature 5
from src.repositories.movie_repository import get_movie_repository

movie_repository = get_movie_repository()

def test_update_movie():
    movie = movie_repository.create_movie("Test Movie", "Test Director", 5)
    updated_movie = movie_repository.update_movie(movie.movie_id, "Updated Test Movie", "Updated Test Director", 4)
    assert updated_movie.title == "Updated Test Movie"
    assert updated_movie.director == "Updated Test Director"
    assert updated_movie.rating == 4