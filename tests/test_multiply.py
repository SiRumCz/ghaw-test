"""Tests for the ``multiply`` function."""

from calculator import multiply


def test_multiply():
    assert multiply(3, 4) == 12
    assert multiply(-2, 3) == -6
    assert multiply(0, 100) == 0
    assert multiply(2.5, 2) == 5.0
