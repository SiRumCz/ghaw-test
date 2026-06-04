"""Tests for the ``modulo`` function."""

import pytest

from calculator import modulo


def test_modulo():
    assert modulo(10, 3) == 1
    assert modulo(9, 3) == 0
    assert modulo(7, 4) == 3
    assert modulo(-7, 4) == 1


def test_modulo_by_zero():
    with pytest.raises(ValueError, match="Cannot take modulo by zero"):
        modulo(10, 0)
