import re  # Import the 're' module for regular expressions
import sys  # Import the 'sys' module for system-related operations


def main():
    # Get user input and call the 'count' function to find and count occurrences of "um"
    print(count(input("Text: ")))


def count(s):
    # Define a regular expression pattern to find instances of "um" with optional punctuation or spaces
    # \b ensures "um" is a whole word, \?|\s|'|\.''|,|.+|$ match various possible endings
    pattern = r"\bum\b(\?|\s|'|\.''|,|.+|$)"
    # Find all matches of the pattern in the input string
    matches = re.findall(pattern, s, re.IGNORECASE)
    return len(matches)  # Return the count of matches


if __name__ == "__main__":
    main()  # Call the main function to start the program
