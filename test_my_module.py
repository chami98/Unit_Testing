import pytest
from my_module import add, subtract

def test_add():
    # Test the add function with some test cases
    assert add(2, 3) == 5
    assert add(-1, 5) == 4
    assert add(0, 0) == 0
    assert add(0, -1) == -1
    assert add(100, -100) == 0

def test_subtract():
    # Test the subtract function with some test cases
    assert subtract(5, 3) == 2
    assert subtract(0, 0) == 0
    assert subtract(-5, 3) == -8
    assert subtract(10, 5) == 5
    assert subtract(-10, -5) == -5

def test_add_subtract_combined():
    # Test both add and subtract functions together
    assert add(3, 5) == 8
    assert subtract(10, 2) == 8
    assert add(2, subtract(10, 5)) == 7
