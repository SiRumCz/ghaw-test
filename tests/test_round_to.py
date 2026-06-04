"""Tests for the ``round_to`` function."""

from calculator import round_to


def test_round_to():
    assert round_to(3.14159, 2) == 3.14
    assert round_to(2.675, 2) == 2.68
    assert round_to(1.5, 0) == 2
    assert round_to(2.5, 0) == 3
