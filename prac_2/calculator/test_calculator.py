"""Тесты для функций калькулятора."""

from calculator import add_numbers


def test_add_positive():
    """2 + 3 должно быть 5."""
    assert add_numbers(2, 3) == 5


def test_add_negative():
    """-2 + (-3) должно быть -5."""
    assert add_numbers(-2, -3) == -5


def test_add_zero():
    """0 + 0 должно быть 0."""
    assert add_numbers(0, 0) == 0


def test_add_floats():
    """0.1 + 0.2 — работа с дробями."""
    result = add_numbers(0.1, 0.2)
    assert abs(result - 0.3) < 1e-9