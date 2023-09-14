# Import the 'convert' function from the 'working' module.
from working import convert
import pytest  # Import the 'pytest' module for testing.


def main():
    test_convert()
    test_convert_raise()


def test_convert():
    # Test cases for valid time conversion.
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"
    assert convert("10 PM to 8 AM") == "22:00 to 08:00"
    assert convert("10:30 PM to 8:50 AM") == "22:30 to 08:50"


def test_convert_raise():
    # Test cases for raising ValueError.
    with pytest.raises(ValueError):
        convert("9:60 AM to 5:60 PM")  # Invalid minutes in time.
    with pytest.raises(ValueError):
        convert("9 AM - 5 PM")  # Invalid time range format.
    with pytest.raises(ValueError):
        convert("09:00 AM - 17:00 PM")  # Invalid time range format.
    with pytest.raises(ValueError):
        convert("09:00 AM 17:00 PM")  # Invalid time range format.


if __name__ == "__main__":
    main()  # Call the main function to start the testing.
