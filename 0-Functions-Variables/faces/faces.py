def main():
    """
    This function takes user input, converts it using the convert function,
    and then prints the converted string.

    Usage:
    1. Run the program.
    2. Enter a string when prompted.
    3. The program will print the converted string.
    """
    # Prompt the user to enter a string
    string = input("Enter a string: ")
    # Convert the string using the convert function
    converted_string = convert(string)
    # Print the converted string
    print(converted_string)


def convert(string):
    """
    This function replaces ":)" with "🙂" and ":(" with "🙁" in the input string.

    Parameters:
    - string (str): The input string to be converted.

    Returns:
    - str: The converted string.
    """
    # Replace ":)" with "🙂" in the string
    string = string.replace(":)", "🙂")
    # Replace ":(" with "🙁" in the string
    string = string.replace(":(", "🙁")
    # Return the converted string
    return string


# Call the main function
main()
