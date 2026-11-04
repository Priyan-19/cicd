"""
Unit tests for the Calculator class.
"""
import pytest
from app.calculator import Calculator


def test_add():
    assert Calculator.add(2, 3) == 5
    assert Calculator.add(-1, 1) == 0
    assert Calculator.add(-2, -3) == -5


def test_subtract():
    assert Calculator.subtract(10, 5) == 5
    assert Calculator.subtract(0, 5) == -5
    assert Calculator.subtract(-5, -5) == 0


def test_multiply():
    assert Calculator.multiply(3, 4) == 12
    assert Calculator.multiply(-2, 3) == -6
    assert Calculator.multiply(5, 0) == 0


def test_divide():
    assert Calculator.divide(10, 2) == 5
    assert Calculator.divide(7, 2) == 3.5
    assert Calculator.divide(-10, 2) == -5


def test_divide_by_zero():
    # Verify that dividing by zero raises a ValueError
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        Calculator.divide(10, 0)
    

def test_power():
    assert Calculator.power(2, 3) == 8
    assert Calculator.power(5, 0) == 1
    assert Calculator.power(2, -1) == 0.5