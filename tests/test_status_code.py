import requests


def test_url_status(url, code):
    response = requests.get(url)
    assert response.status_code == code

