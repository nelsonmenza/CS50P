from um import count  # Import the 'count' function from the 'um' module


def main():
    # Run the test functions
    test_count()
    test_count_fail()


def test_count():
    # Test cases for the 'count' function
    assert count("um?") == 1  # Should find 1 occurrence of 'um'
    assert count("um") == 1  # Should find 1 occurrence of 'um'
    # Should find 1 occurrence of 'um'
    assert count("Um, thanks for the album.") == 1
    # Should find 2 occurrences of 'um'
    assert count(
        "Um? Mum? Is this that album where, um, umm, the clumsy alums play drums?") == 2
    assert count("Um, thanks, um...") == 2  # Should find 2 occurrences of 'um'


def test_count_fail():
    # Test cases for the 'count' function where 'um' should not be found
    assert count("yummy") == 0  # Should not find any occurrence of 'um'
    assert count("Album") == 0  # Should not find any occurrence of 'um'
    assert count("Plum") == 0  # Should not find any occurrence of 'um'
    assert count("Humble") == 0  # Should not find any occurrence of 'um'


if __name__ == "__main__":
    main()  # Call the main function to run the tests
