import pytest

class DataProcessor():
    def cap_words(self, string: str):
        self.string = string
        return self.string.title()
    
    def reverse_it(self, items: list):
        self.items = items
        return self.items[::-1]
    

def test_cap_words():
    data = DataProcessor()
    assert data.cap_words("") == ""
    assert data.cap_words("hello") == "Hello"
    assert data.cap_words("heLlo worlD") == "Hello World"
    
def test_reverse_it():
    data = DataProcessor()
    assert data.reverse_it([1, 2, 3]) == [3, 2, 1]
    assert data.reverse_it("abc") == "cba"
    assert data.reverse_it(["a", "b", "c"]) == ["c", "b", "a"]
    assert data.reverse_it([1, "a"]) == ["a", 1]

