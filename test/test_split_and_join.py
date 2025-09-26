import pytest, time
from src.split_and_join import split_and_join

@pytest.mark.parametrize("input_line, expected", [
    pytest.param("This is a test", "This-is-a-test", id='"This is a test", "This-is-a-test"'),
    pytest.param("Hello World", "Hello-World", id='"Hello World", "Hello-World"'),
    pytest.param("Python is great", "Python-is-great", id='"Python is great", "Python-is-great"'),
    pytest.param("quick brown fox jumps over a lazy dog", "quick-brown-fox-jumps-over-a-lazy-dog", id='"quick brown fox jumps over a lazy dog", "quick-brown-fox-jumps-over-a-lazy-dog"'),
])

def test_split_and_join(input_line, expected):
    assert split_and_join(input_line) == expected
