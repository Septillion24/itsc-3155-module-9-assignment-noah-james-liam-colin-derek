# TODO: Feature 3
from src.models.movie import Movie


def test_get_movie_by_title(self):
    movie = self.repo.create_movie("Test Movie", "Test Director", 5)
    retrieved_movie = self.repo.get_movie_by_title("Test Movie")
    self.assertEqual(movie, retrieved_movie)
