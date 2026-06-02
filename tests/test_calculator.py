"""
Tests for the calculator module.
"""
import pytest
import sys
from pathlib import Path

# Add src to path
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from calculator import add, subtract, multiply, divide, power


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
