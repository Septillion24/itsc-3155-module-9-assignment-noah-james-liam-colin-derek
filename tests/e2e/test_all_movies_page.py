from app import app

def test_all_movies_blank():
    test_app = app.test_client()
    response = test_app.get('/movies')
    assert 200 == response.status_code



