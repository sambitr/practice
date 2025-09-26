import pytest
from src.two_sum import two_sum

# @pytest.mark.parametrize("a,b,expected", [(2,3,5), (-1,1,0), (0,0,0)])
# def test_sum_int(a, b, expected):
#     assert two_sum(a, b) == expected
def test_sum_int():
    assert two_sum(2, 3) == 5
    assert two_sum(-1, 1) == 0
    assert two_sum(0, 0) == 0

def test_sum_str():
    assert two_sum("a", "A") == "aA"
    assert two_sum("Hello, ", "World!") == "Hello, World!"

def test_type_error():
    with pytest.raises(TypeError):
        two_sum("1", 2)