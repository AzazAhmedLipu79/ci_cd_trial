import pytest

def test_addition():
    assert 1 + 1 == 2

def test_subtraction():
    assert 5 - 3 == 2

def test_multiplication():
    assert 2 * 0 == 0

def test_division(): 
    assert 10 / 2 == 5

def test_division_by_zero():
    with pytest.raises(ZeroDivisionError):
        1 / 0



