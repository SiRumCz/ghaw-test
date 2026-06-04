"""Tests for the ``abs`` function."""

from calculator import abs


def test_abs():
    assert abs(5) == 5
    assert abs(-5) == 5
    assert abs(0) == 0
    assert abs(-2.5) == 2.5
