def main():
    # Prompt the user to enter a string
    string = input("Enter a string: ")
    # Convert the string using the convert function
    converted_string = convert(string)
    # Print the converted string
    print(converted_string)


def convert(string):
    # Replace ":)" with "🙂" in the string
    string = string.replace(":)", "🙂")
    # Replace ":(" with "🙁" in the string
    string = string.replace(":(", "🙁")
    # Return the converted string
    return string


# Call the main function
main()
