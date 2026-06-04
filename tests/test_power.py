"""Tests for the ``power`` function."""

from calculator import power


def test_power():
    assert power(2, 3) == 8
    assert power(5, 0) == 1
    assert power(10, 2) == 100
    assert power(2, -1) == 0.5
