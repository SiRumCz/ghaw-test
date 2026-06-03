"""
Tests for the calculator module.
"""

import sys
from pathlib import Path

import pytest

# Add src to path
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from calculator import (
    abs,
    add,
    clamp,
    divide,
    integer_divide,
    modulo,
    multiply,
    power,
    round_to,
    sqrt,
    subtract,
)


class TestCalculator:
    """Test cases for calculator functions."""

    def test_add(self):
        assert add(2, 3) == 5
        assert add(-1, 1) == 0
        assert add(0, 0) == 0
        assert add(1.5, 2.5) == 4.0

    def test_subtract(self):
        assert subtract(5, 3) == 2
        assert subtract(0, 5) == -5
        assert subtract(10, 10) == 0
        assert subtract(3.5, 1.5) == 2.0

    def test_multiply(self):
        assert multiply(3, 4) == 12
        assert multiply(-2, 3) == -6
        assert multiply(0, 100) == 0
        assert multiply(2.5, 2) == 5.0

    def test_divide(self):
        assert divide(10, 2) == 5
        assert divide(9, 3) == 3
        assert divide(5, 2) == 2.5
        assert divide(-10, 2) == -5

    def test_divide_by_zero(self):
        with pytest.raises(ValueError, match="Cannot divide by zero"):
            divide(10, 0)

    def test_power(self):
        assert power(2, 3) == 8
        assert power(5, 0) == 1
        assert power(10, 2) == 100
        assert power(2, -1) == 0.5

    def test_modulo(self):
        assert modulo(10, 3) == 1
        assert modulo(9, 3) == 0
        assert modulo(7, 4) == 3
        assert modulo(-7, 4) == 1

    def test_modulo_by_zero(self):
        with pytest.raises(ValueError, match="Cannot take modulo by zero"):
            modulo(10, 0)

    def test_integer_divide(self):
        assert integer_divide(10, 3) == 3
        assert integer_divide(9, 3) == 3
        assert integer_divide(7, 2) == 3
        assert integer_divide(-7, 2) == -4

    def test_integer_divide_by_zero(self):
        with pytest.raises(ValueError, match="Cannot divide by zero"):
            integer_divide(10, 0)

    def test_sqrt(self):
        assert sqrt(4) == 2
        assert sqrt(9) == 3
        assert sqrt(0) == 0
        assert sqrt(2) == pytest.approx(1.4142135623730951)

    def test_sqrt_negative(self):
        with pytest.raises(
            ValueError, match="Cannot take square root of a negative number"
        ):
            sqrt(-1)

    def test_abs(self):
        assert abs(5) == 5
        assert abs(-5) == 5
        assert abs(0) == 0
        assert abs(-2.5) == 2.5

    def test_clamp(self):
        assert clamp(5, 0, 10) == 5
        assert clamp(-1, 0, 10) == 0
        assert clamp(15, 0, 10) == 10
        assert clamp(5, 5, 5) == 5

    def test_clamp_invalid_range(self):
        with pytest.raises(
            ValueError, match="min_value cannot be greater than max_value"
        ):
            clamp(5, 10, 0)

    def test_round_to(self):
        assert round_to(3.14159, 2) == 3.14
        assert round_to(2.675, 2) == 2.68
        assert round_to(1.5, 0) == 2
        assert round_to(2.5, 0) == 3
