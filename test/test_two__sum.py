import pytest
from src.two_sum import two_sum

@pytest.mark.parametrize("a,b,expected", [(2,3,5), (-1,1,0), (0,0,0)])
def test_sum_param(a, b, expected):
    assert two_sum(a, b) == expected

def test_type_error():
    with pytest.raises(TypeError):
        two_sum("1", 2)