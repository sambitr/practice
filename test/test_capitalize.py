import pytest
from src.capitalize import solve


@pytest.mark.parametrize("input_string, result", [
    ("chris alan", "Chris Alan"),
    ("1 w 2 r 3g", "1 W 2 R 3G"),
    ("hello world", "Hello World"),
])

def test_solve(input_string, result):
    assert solve(input_string) == result