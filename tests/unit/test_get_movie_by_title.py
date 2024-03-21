# TODO: Feature 3
from src.models.movie import Movie


def test_get_movie_by_title():
    movie = Movie(456, "Ferris Bueller's Day Off", 'John Hughes', 4)

    assert movie.title == "Ferris Bueller's Day Off"
