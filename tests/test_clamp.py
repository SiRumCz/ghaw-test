"""Tests for the ``clamp`` function."""

import pytest

from calculator import clamp


def test_clamp():
    assert clamp(5, 0, 10) == 5
    assert clamp(-1, 0, 10) == 0
    assert clamp(15, 0, 10) == 10
    assert clamp(5, 5, 5) == 5


def test_clamp_invalid_range():
    with pytest.raises(ValueError, match="min_value cannot be greater than max_value"):
        clamp(5, 10, 0)
