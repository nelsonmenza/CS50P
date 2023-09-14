"""
This program prompts the user to enter a camelCase string, converts it to snake_case, and prints the snake_case version of the input string.

Usage:
1. Run the program.
2. Enter a camelCase string when prompted.
3. The program will convert the camelCase string to snake_case and print the snake_case version.

Example:
camelCase: myVariableName
snake_case: my_variable_name
"""

# Prompt the user to enter a camelCase string
camelCase = input("camelCase: ")
# Initialize an empty string to store the snake_case version
snake_case = ""
# Iterate through each character in the camelCase string
for char in range(len(camelCase)):
    # Check if the current character is not uppercase
    if camelCase[char] != camelCase[char].upper():
        # Append the current character to the snake_case string
        snake_case = snake_case + camelCase[char]
    else:
        # Append an underscore followed by the lowercase version of the current character to the snake_case string
        snake_case = snake_case + "_" + camelCase[char].lower()
 # Print the snake_case version of the input string
print("snake_case: ", snake_case)
