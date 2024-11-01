import requests
from random import choice

def fetch_data(url, params=""):
    # fetch API date
    response = requests.get(url, params=params)
    response.raise_for_status()
    return response.json()

def test_fetch_data():
    # Satirical Chuck Norris Jokes API (yep, it exists)
    endpoint = "/jokes/random"
    url = "https://api.chucknorris.io" + endpoint
    # API supports several joke categories
    categories = ["dev", "movie", "animal", "career"]
    # choose the category for joke as a provided param
    params = {"category": f"{choice(categories)}"}

    data = fetch_data(url, params)
    # print(data)
    # response ID must have a length greater than 0
    assert len(data["id"]) > 0
    # response must have the same category as the request
    assert data["categories"][0] in params["category"]
    # value in response object must be of type string
    assert isinstance(data["value"], str)

    
from unittest.mock import patch

@patch("requests.get")
def test_fetch_data_mocked(mock_get):
    # define all variables, endpoints and parameters first as we'll need them when composing our mock response
    
    # Satirical Chuck Norris Jokes API (yep, it exists)
    endpoint = "/jokes/random"
    url = "https://api.chucknorris.io" + endpoint
    # API supports several joke categories
    categories = ["dev", "movie", "animal", "career"]
    # choose the category for joke as a provided param
    params = {"category": f"{choice(categories)}"}
    
    # compose the response so that the 'categories' value match the value in the requests 'param'
    mock_response = {'categories': [f'{params["category"]}'],
                     'created_at': '2020-01-05 13:42:19.324003',
                     'icon_url': 'https://api.chucknorris.io/img/avatar/chuck-norris.png',
                     'id': 'dpk2_epftfgo0cgpfqcpgq',
                     'updated_at': '2020-01-05 13:42:19.324003',
                     'url': 'https://api.chucknorris.io/jokes/dpk2_epftfgo0cgpfqcpgq',
                     'value': 'Chuck Norris can install iTunes without installing Quicktime.'
    }
    mock_get.return_value.json.return_value = mock_response
    
    # call the tested function next
    data = fetch_data(url, params)

    # response ID must have a length greater than 0
    assert len(data["id"]) > 0
    # response must have the same category as the request
    # print(data["categories"][0], "\n", params["category"])
    assert data["categories"][0] in params["category"]
    # value in response object must be of type string
    assert isinstance(data["value"], str)
    
    mock_get.assert_called_once_with(url, params=params)
