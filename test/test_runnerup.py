import pytest
from src.runnerup import find_runner_up

@pytest.mark.parametrize("participants, result_in_array, expected", [
    pytest.param(5, [2, 3, 6, 6, 5], 5, id='5_participants_[2,3,6,6,5]_expected_5'),
    pytest.param(4, [3, 1, 2, 2], 2, id='4_participants_[3,1,2,2]_expected_2'),
    pytest.param(3, [10, 10, 10], None, id='3_participants_[10,10,10]_expected_None'),
    pytest.param(6, [1, 2, 3, 4, 5, 6], 5, id='6_participants_[1,2,3,4,5,6]_expected_5'),
    pytest.param(7, [7, 7, 7, 7, 7, 7, 7], None, id='7_participants_[7,7,7,7,7,7,7]_expected_None'),
    pytest.param(2, [1, 2, 1], "Number of participants and results do not match", id='2_participants_[1,2,1]_expected_mismatch'),
])

def test_find_runner_up(participants, result_in_array, expected):
    assert find_runner_up(participants, result_in_array) == expected