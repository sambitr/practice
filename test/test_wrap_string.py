import pytest
from src.wrap_string import wrap_string

@pytest.mark.parametrize("input_string, width, expected_output", [
    ("ABCDEFGHIJKLIMNOQRSTUVWXYZ", 4, ["ABCD", "EFGH", "IJKL", "IMNO", "QRST", "UVWX", "YZ"]),
    ("HelloWorld", 2, ["He", "ll", "oW", "or", "ld"]),
    ("PythonTesting", 3, ["Pyt", "hon", "Tes", "tin", "g"]),
    ("", 5, []),
])
def test_wrap_string(input_string, width, expected_output, capsys):
    wrap_string(input_string, width)
    captured = capsys.readouterr().out.splitlines()
    assert captured == expected_output