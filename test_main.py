import pytest
from main import is_three_digit, sum_three_values, get_three_digit_input


def test_is_three_digit_valid():
    assert is_three_digit(100) is True
    assert is_three_digit(500) is True
    assert is_three_digit(999) is True


def test_is_three_digit_invalid():
    assert is_three_digit(99) is False
    assert is_three_digit(1000) is False
    assert is_three_digit(0) is False
    assert is_three_digit(-100) is False


def test_sum_three_values():
    assert sum_three_values(100, 200, 300) == 600
    assert sum_three_values(999, 999, 999) == 2997
    assert sum_three_values(100, 100, 100) == 300


def test_get_three_digit_input_valid(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: "123")
    assert get_three_digit_input("Enter: ") == 123


def test_get_three_digit_input_invalid_low(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: "99")
    with pytest.raises(ValueError):
        get_three_digit_input("Enter: ")


def test_get_three_digit_input_invalid_high(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: "1000")
    with pytest.raises(ValueError):
        get_three_digit_input("Enter: ")


def test_get_three_digit_input_non_numeric(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: "abc")
    with pytest.raises(ValueError):
        get_three_digit_input("Enter: ")
