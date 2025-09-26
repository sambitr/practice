import pytest
from src.pallindrome_checker import pallindrome_checker

@pytest.mark.parametrize("input_string, expected", [
    ("A man, a plan, a canal: Panama", True),
    ("race a car", False),
    ("No 'x' in Nixon", True),
    ("Sambit", False)
])
def test_pallindrome_checker(input_string, expected):
    assert pallindrome_checker(input_string) == expected