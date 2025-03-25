import pytest

from execute_addition import add

def test_execute_addition():
    x = 5
    y = 4
    expected = x + y

    actual = add(x, y)

    assert (expected == actual)
