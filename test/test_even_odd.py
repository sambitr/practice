import pytest
import src.even_odd as eo

def test_evenOddNumber():
    assert eo.evenOddNumber(4) == "Even"
    assert eo.evenOddNumber(5) == "Odd"
    assert eo.evenOddNumber("Hello") == "Invalid Input"