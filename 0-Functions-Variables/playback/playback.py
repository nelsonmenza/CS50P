"""
This program takes a user-input string, removes spaces from it, and replaces each space with "..."
in the modified string. The modified string is then printed.

Usage:
1. Run the program.
2. Enter a string when prompted.
3. The program will remove spaces from the input string and print the modified string.

Example:
Enter a string: This is a test
This...is...a...test
"""
# Prompt the user to enter a string and store it in the variable 'indoor'
playback = input("Enter a string: ")
# Initialize an empty string to store the modified string
new_string = ""
# Iterate through each character in the input string
for i in range(len(playback)):
    # Check if the current character is not a space
    if playback[i] != " ":
        # If it is not a space, add it to the new string
        new_string += playback[i]
    else:
        # If it is a space, add "..." to the new string
        new_string += "..."
 # Print the modified string
print(new_string)
