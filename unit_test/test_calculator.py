from .calculator import square
import pytest


def test_positives():
    assert square(2) == 4
    assert square(3) == 9

def test_negatives():
    assert square(-2) == 4
    assert square(-3) == 9

def test_zero():
    assert square(0) == 0

def test_string():
    with pytest.raises(TypeError):
        square('cat')