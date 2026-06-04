"""Tests for the ``divide`` function."""

import pytest

from calculator import divide


def test_divide():
    assert divide(10, 2) == 5
    assert divide(9, 3) == 3
    assert divide(5, 2) == 2.5
    assert divide(-10, 2) == -5


def test_divide_by_zero():
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        divide(10, 0)
