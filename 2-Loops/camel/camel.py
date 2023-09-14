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
