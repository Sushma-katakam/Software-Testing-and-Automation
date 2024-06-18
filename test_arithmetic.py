""" test_arithmetic.py initial file """

import pytest
from arithmetic import add, subtract, multiply, divide

def test_add():
    """ Test add function """
    assert add(1, 2) == 3

def test_subtract():
    """ Test substraction function"""
    assert subtract(2, 1) == 1

def test_multiply():
    """ Test multiply function"""
    assert multiply(2, 3) == 6

def test_divide():
    """ Test divide function"""
    assert divide(6, 2) == 3

def test_divide_by_zero():
    """ Test divide by zero """
    with pytest.raises(ValueError):
        divide(1, 0)
