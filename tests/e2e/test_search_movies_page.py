# TODO: Feature 3
from flask.testing import FlaskClient

def test_search_page(test_app: FlaskClient):
    response = test_app.get('/movies/search')
    response_data = response.data.decode('utf-8')

    assert '<h1 class="mb-5">Search Movie Ratings</h1>' in response_data
