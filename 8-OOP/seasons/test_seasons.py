from datetime import date, timedelta, datetime
import sys
import inflect
import pytest
from io import StringIO
from seasons import DateCalculator, get_date, get_min, main

# Initialize inflect engine
p = inflect.engine()


def test_get_date(monkeypatch):
    # Mock user input for testing
    input_values = ['2000-01-01\n']
    monkeypatch.setattr(sys, 'stdin', StringIO('\n'.join(input_values)))

    delta = get_date()
    # Expected output: Number of seconds between today and 2000-01-01
    expected_seconds = 745632000.0
    assert delta.total_seconds() == expected_seconds


def test_get_min():
    delta = date.today() - date(2000, 1, 1)
    minutes = get_min(delta)
    # Expected output: Number of minutes between today and 2000-01-01
    assert minutes == 12427200


def test_date_calculator_str():
    calc = DateCalculator(123)
    # Expected output: "One hundred twenty-three minutes"
    assert str(calc) == "One hundred twenty-three minutes"


if __name__ == "__main__":
    pytest.main()
