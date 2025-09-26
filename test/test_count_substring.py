import pytest
from src.count_substring import count_substring


@pytest.mark.parametrize("string, substring, expected", [
    ("ABCDCDC", "CDC", 2),
    ("AAAAA", "AA", 4)
])
def test_count_substring(string, substring, expected):
    assert count_substring(string, substring) == expected
