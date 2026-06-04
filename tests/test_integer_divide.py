"""Tests for the ``integer_divide`` function."""

import pytest

from calculator import integer_divide


def test_integer_divide():
    assert integer_divide(10, 3) == 3
    assert integer_divide(9, 3) == 3
    assert integer_divide(7, 2) == 3
    assert integer_divide(-7, 2) == -4


def test_integer_divide_by_zero():
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        integer_divide(10, 0)
