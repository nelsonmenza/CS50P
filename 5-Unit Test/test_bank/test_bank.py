from bank import value  # Import the value function from the bank module.


def main():
    # Call the three test functions to test different return values.
    test_return_0()
    test_return_20()
    test_return_100()


def test_return_0():
    # Test cases for values that should return 0.
    assert value("Hello") == 0
    assert value("hello") == 0
    assert value("HELLO") == 0


def test_return_20():
    # Test cases for values that should return 20.
    assert value("hi") == 20
    assert value("Hey") == 20


def test_return_100():
    # Test cases for values that should return 100.
    assert value("What's up?") == 100
    assert value("Morning!") == 100


if __name__ == "__main__":
    main()  # Call the main function to run the tests.
