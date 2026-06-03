"""
A simple calculator module for testing GitHub agentic workflows.
"""

import math
from decimal import ROUND_HALF_UP, Decimal


def add(a: float, b: float) -> float:
    """Add two numbers."""
    return a + b


def subtract(a: float, b: float) -> float:
    """Subtract b from a."""
    return a - b


def multiply(a: float, b: float) -> float:
    """Multiply two numbers."""
    return a * b


def divide(a: float, b: float) -> float:
    """Divide a by b."""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


def power(base: float, exponent: float) -> float:
    """Raise base to the power of exponent."""
    return base**exponent


def modulo(a: float, b: float) -> float:
    """Return the remainder of a divided by b."""
    if b == 0:
        raise ValueError("Cannot take modulo by zero")
    return a % b


def integer_divide(a: float, b: float) -> float:
    """Return the integer (floor) division of a by b."""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a // b


def sqrt(n: float) -> float:
    """Return the square root of n."""
    if n < 0:
        raise ValueError("Cannot take square root of a negative number")
    return math.sqrt(n)


def abs(n: float) -> float:
    """Return the absolute value of n."""
    return -n if n < 0 else n


def clamp(n: float, min_value: float, max_value: float) -> float:
    """Constrain n to the inclusive range [min_value, max_value]."""
    if min_value > max_value:
        raise ValueError("min_value must not be greater than max_value")
    if n < min_value:
        return min_value
    if n > max_value:
        return max_value
    return n


def round_to(n: float, decimals: int = 0) -> float:
    """Round n to the given number of decimal places using half-up rounding."""
    if decimals < 0:
        raise ValueError("decimals must be non-negative")
    quantum = Decimal(1).scaleb(-decimals)
    return float(Decimal(str(n)).quantize(quantum, rounding=ROUND_HALF_UP))
