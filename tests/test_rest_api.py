import pytest
import requests

@pytest.mark.duckduckgo
@pytest.mark.rest_api
def test_duck_duck_go_api():

    url = "https://api.duckduckgo.com/?q=Python+Programming&format=json"
    response = requests.get(url)
    body = response.json()

    #assert
    assert response.status_code == 200
    print(body['AbstractText'])
    assert 'Python' in body['AbstractText']
