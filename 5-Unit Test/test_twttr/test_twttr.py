# Import the "shorten" function from the "twttr" module.
from twttr import shorten

# Test basic string shortening with vowel removal.


def test_shorten_basic():
    assert shorten("douleia") == "dl"
    assert shorten("suoidea") == "sd"
    assert shorten("eutopia") == "tp"
    assert shorten("other") == "thr"

# Test string shortening with included numbers.


def test_shorten_with_numbers():
    assert shorten("do2ulei3a") == "d2l3"
    assert shorten("suo5ide00a") == "s5d00"
    # Numbers-only input should remain unchanged.
    assert shorten("12345") == "12345"

# Test shortening an empty string.


def test_shorten_empty_string():
    assert shorten("") == ""

# Test shortening capitalized strings.


def test_shorten_capitalized():
    assert shorten("DoUleia") == "Dl"
    assert shorten("SuOiDEa") == "SD"
    assert shorten("EUtoPia") == "tP"
    assert shorten("OtHER") == "tHR"

# Test shortening strings with special characters.


def test_shorten_special_characters():
    assert shorten("dou,.leia") == "d,.l"
    assert shorten("s<.>uoid;'[ea") == "s<.>d;'["
    assert shorten("eu%&top@#$ia") == "%&tp@#$"
    assert shorten("o-=+t-///-he**/r") == "-=+t-///-h**/r"

# You can add more specific test cases based on possible edge cases or scenarios.

# Run all the defined tests.


def run_tests():
    test_shorten_basic()
    test_shorten_with_numbers()
    test_shorten_empty_string()
    test_shorten_capitalized()
    test_shorten_special_characters()
    print("All tests passed!")


if __name__ == "__main__":
    run_tests()  # Call the function to run the tests.
