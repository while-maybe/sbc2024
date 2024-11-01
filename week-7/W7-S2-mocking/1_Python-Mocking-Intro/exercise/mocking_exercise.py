import requests

def fetch_data(url):
    """fetch data from an API"""
    response = requests.get(url)
    response.raise_for_status()
    return response.json()

def test_fetch_data():
    url = "https://catfact.ninja/fact"
    data = fetch_data(url)
    # check if the key ["fact"]
    print(data["fact"])
    assert isinstance(data["fact"], str)
    assert data["length"] > 0


from unittest.mock import patch

@patch("requests.get")
def test_fetch_data_mocked(mock_get):
    
    mock_get.return_value.json.return_value = {
        "fact": "Approximately 1\/3 of cat owners think their pets are able to read their minds.",
        "length": 78
    }
    
    # Call the tested function
    url = "https://catfact.ninja/fact"
    data = fetch_data(url)
    
    # check results
    assert isinstance(data["fact"], str)
    assert data["length"] > 0
    
    mock_get.assert_called_once_with(url)
