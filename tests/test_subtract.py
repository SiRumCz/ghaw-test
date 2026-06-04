"""Tests for the ``subtract`` function."""

from calculator import subtract


def test_subtract():
    assert subtract(5, 3) == 2
    assert subtract(0, 5) == -5
    assert subtract(10, 10) == 0
    assert subtract(3.5, 1.5) == 2.0
