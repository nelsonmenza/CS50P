# Import the is_valid function from the plates module.
from plates import is_valid


def main():
    test_zero()
    test_start()
    test_length()
    test_numbers()
    test_punc()

# Test function for starting character requirements.


def test_start():
    assert is_valid('ABCDEF') == True  # Valid: Starts with two letters.
    assert is_valid('1ABCDE') == False  # Invalid: Starts with a number.
    # Invalid: Starts with a letter followed by a number.
    assert is_valid('A3CDEF') == False
    assert is_valid('63CDEF') == False  # Invalid: Starts with a number.

# Test function for including numbers.


def test_numbers():
    assert is_valid('ABC123') == True  # Valid: Contains numbers at the end.
    assert is_valid('ABCD12') == True  # Valid: Contains numbers at the end.
    assert is_valid('ABCDE1') == True  # Valid: Contains numbers at the end.
    # Invalid: Contains numbers in the middle.
    assert is_valid('AB23EF') == False
    # Invalid: Contains numbers in the middle.
    assert is_valid('ABC23F') == False
    assert is_valid("AA") == True  # Valid: No numbers.
    # Invalid: Starts with a letter followed by a number.
    assert is_valid("A2") == False
    assert is_valid("2A") == False  # Invalid: Starts with a number.
    assert is_valid("22") == False  # Invalid: Starts with a number.
    assert is_valid(" 2") == False  # Invalid: Starts with a number.

# Test function for zero placement.


def test_zero():
    assert is_valid('ABC102') == True  # Valid: Zero at the end.
    assert is_valid('CS50') == True  # Valid: No zeros.
    assert is_valid('ABC012') == False  # Invalid: Zero at the beginning.
    assert is_valid('ABCD01') == False  # Invalid: Zero at the beginning.

# Test function for punctuation restrictions.


def test_punc():
    assert is_valid('ABC,23') == False  # Invalid: Contains comma.
    assert is_valid('ABC 23') == False  # Invalid: Contains space.
    assert is_valid('ABC.12') == False  # Invalid: Contains period.
    assert is_valid('AB:12') == False  # Invalid: Contains colon.
    assert is_valid('AB/45') == False  # Invalid: Contains forward slash.

# Test function for length requirements.


def test_length():
    assert is_valid('ABCDEF') == True  # Valid: 6 characters.
    assert is_valid('ABCDE') == True  # Valid: 5 characters.
    assert is_valid('ABC') == True  # Valid: 3 characters.
    assert is_valid('AB') == True  # Valid: 2 characters.
    assert is_valid('A') == False  # Invalid: 1 character.


# Run all the test functions when this script is executed directly.
if __name__ == "__main__":
    main()
