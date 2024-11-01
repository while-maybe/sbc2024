class Database:
    """Database class"""
    def connect(self):
        """Simulates connecting to DB"""
        raise NotImplementedError("This method should connect to database")
    
    def fetch_data(self, query):
        """Simulates fetching data"""
        raise NotImplementedError("This method should fetch data based on the query")
    
class DataService:
    """Service that uses Database class to fetch data"""

    def __init__(self, db: Database):
        self.db = db

    def get_user_data(self, user_id):
        """Fetches user data based on user_id"""
        query = f"SELECT * FROM users WHERE id={user_id}"
        return self.db.fetch_data(query)


from unittest.mock import Mock

def test_get_user_data():
    """Test the DataService.get_user_data method using a mock object"""
    
    # create the mock object
    mock_database = Mock(spec=Database)
    
    # define behaviour of the fetch_data method
    mock_database.fetch_data.return_value = {"id": 1, "name": "Alice"}
    
    # create an instance of DataService with the mock DataBase
    service = DataService(mock_database)
    
    # call the method we're testing
    result = service.get_user_data(1)
    
    # Assert results
    assert result["id"] == 1
    assert result["name"] == "Alice"
    
    # Verify that fetch_data method was called wit the correct query
    mock_database.fetch_data.assert_called_once_with("SELECT * FROM users WHERE id=1")
    