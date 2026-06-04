"""Tests for the ``sqrt`` function."""

import pytest

from calculator import sqrt


def test_sqrt():
    assert sqrt(4) == 2
    assert sqrt(9) == 3
    assert sqrt(0) == 0
    assert sqrt(2) == pytest.approx(1.4142135623730951)


def test_sqrt_negative():
    with pytest.raises(
        ValueError, match="Cannot take square root of a negative number"
    ):
        sqrt(-1)
