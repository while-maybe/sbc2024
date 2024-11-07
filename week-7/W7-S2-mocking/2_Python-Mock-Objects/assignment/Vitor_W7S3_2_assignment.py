import json
from unittest.mock import Mock

# JSON data was extracted from https://lldev.thespacedevs.com/2.3.0/launches/?search=Starlink&format=json&mode=list


class OnlineData:
    """Simlulated API calls class"""

    def fetch_launches(self, search):
        raise NotImplementedError(
            "This method returns all data from a keyword search - Starlink in this example"
        )

    def fetch_upcoming(self):
        raise NotImplementedError("Returns upcoming launches data only")


class DataService:
    """Service that uses the OnlineData class to fetch data"""

    def __init__(self, api_data: OnlineData):
        self.api_data = api_data

    def get_launches_api_data(self, search):
        search = "Starlink"
        return self.api_data.fetch_launches(search)

    def get_upcoming_api_data(self):
        return self.api_data.fetch_upcoming()


def test_get_launches_api_data():
    # Create a mock API object
    mock_api = Mock(spec=OnlineData)

    # Define Behaviour
    try:
        with open("starlink.json", "r") as file:
            data = json.load(file)
    except FileNotFoundError("Couldn't find starlink data file"):
        return None

    mock_api.fetch_launches.return_value = data

    # Create an instance of DataService with the mock API
    service = DataService(mock_api)

    # call the method under test
    result = service.get_launches_api_data("Starlink")

    # assert some results:
    # assert there's an object count in the data
    assert result["count"] > 0
    # assert results is a list
    assert isinstance(result["results"], list)
    # asserts a there's some text in the first record
    assert isinstance(result["results"][0]["name"], str)
    # checks if the Keyword "Starlink" is in the results
    assert "starlink" in result["results"][0]["name"].lower()

    # call fetch_launches method
    mock_api.fetch_launches("Starlink")


def test_get_upcoming_api_data():
    mock_api = Mock(spec=OnlineData)

    # Define Behaviour
    try:
        with open("upcoming.json", "r") as file:
            data = json.load(file)
    except FileNotFoundError("Couldn't find upcoming launch data file to simulate"):
        return None

    mock_api.fetch_upcoming.return_value = data

    # Create an instance of DataService with the mock API
    service = DataService(mock_api)

    # call the method under test
    result = service.get_upcoming_api_data()

    # assert some results:
    # assert there's an object count in the data
    assert result["count"] > 0
    # assert results is a list
    assert isinstance(result["results"], list)
    # asserts a there's some text in the first record
    assert isinstance(result["results"][0]["name"], str)

    # call fetch_upcoming method
    mock_api.fetch_upcoming()
