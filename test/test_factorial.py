import pytest
from src.factorial import fact

# Use pytest.param(...) to attach ids to parameter sets. You cannot use id= inside a plain tuple.
@pytest.mark.parametrize("input_num, expected", [
    pytest.param(5, 120, id='5, 120'),
    pytest.param(0, 1, id='0, 1'),
    pytest.param(1, 1, id='1, 1'),
    pytest.param(-1, "Invalid Input", id='-1, "Invalid Input"'),
    pytest.param("2", "Invalid Input", id='"2", "Invalid Input"'),
])
def test_factorial(input_num, expected):
    assert fact(input_num) == expected