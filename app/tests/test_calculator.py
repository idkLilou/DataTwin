import pytest

from app.calculator import Calculator


def test_add():
    assert Calculator.add(2, 3) == 5


def test_subtract():
    assert Calculator.subtract(10, 4) == 6


def test_multiply():
    assert Calculator.multiply(3, 4) == 12


def test_divide():
    assert Calculator.divide(12, 3) == 4


def test_divide_by_zero():
    with pytest.raises(ValueError):
        Calculator.divide(10, 0)
