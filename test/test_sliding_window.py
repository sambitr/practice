import pytest
from src.sliding_window import sliding_window

@pytest.mark.parametrize("arr, size_of_slide, expected_result",[
    ([1, 3, -1, -3, 5, 3, 6, 7], 3, 16),
    ([2,1,5,1,3,2], 3, 9),
])

def test_sliding_window(arr, size_of_slide, expected_result):
    assert sliding_window(arr, size_of_slide) == expected_result