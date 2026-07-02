import pytest

# from simple_functions import *
from simple_functions import add, is_even, div, to_positive

def test_add():
    assert add(1, 3) == 4
    assert add(5, -5) == 0
    assert add(0, -1) == -1
    assert add(5, 0.5) == 5.5

def test_is_even():
    assert is_even(5) == False
    assert is_even(0) == True
    assert is_even(-4) == True

def test_div():
    assert div(5, 2) == 2.5
    assert div(10, 2) == 5
    # ne asteptam ca acest div() sa arunce exceptia "ZeroDivisionError"
    #assert div(3, 0) == 0
    with pytest.raises(ZeroDivisionError):
        div(3, 0) == 0

def test_to_positive():
    assert to_positive(-5) == 5
    assert to_positive(-100.5) == 100.5
    assert to_positive(4) == 4
    assert to_positive(-0) == 0
    assert to_positive(0) == 0

    with pytest.raises(TypeError):
        to_positive("50")