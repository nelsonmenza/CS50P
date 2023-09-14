def main():
    string = input("Input:")  # Prompt the user to input a string.
    print(shorten(string))  # Print the string after removing vowels.


def shorten(string):
    new_string = ""  # Initialize an empty string to store the result.
    vowels = "aeiou"  # Define a string containing lowercase vowels.
    for i in string:
        if vowels.find(i) != -1:
            # If the character is a lowercase vowel, do nothing (skip it).
            pass
        elif vowels.upper().find(i) != -1:
            # If the character is an uppercase vowel, do nothing (skip it).
            pass
        else:
            # If the character is not a vowel, add it to 'new_string'.
            new_string = new_string + i
    return new_string  # Return the string with vowels removed.


if __name__ == "__main__":
    main()  # Call the main function to start the program.
