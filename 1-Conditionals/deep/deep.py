"""
This program prompts the user to enter their answer to the Great Question of Life, the Universe, and Everything and checks if their input matches one of the expected answers.

Usage:
1. Run the program.
2. Enter an answer when prompted.
3. The program will check if the entered answer matches "42," "forty two," or "forty-two" (case-insensitive) and print "Yes" if there is a match, or "No" otherwise.

Example:
What is the Answer to the Great Question of Life, the Universe, and Everything? 42
Yes
"""
# Prompt the user to enter their answer to the Great Question of Life, the Universe, and Everything
user_input = input(
    "What is the Answer to the Great Question of Life, the Universe, and Everything? ")
# Check if the user's input is equal to "42" (stripped of leading/trailing whitespace)
if user_input.strip() == "42":
    print("Yes")
# Check if the user's input (converted to lowercase) is equal to "forty two"
elif user_input.lower() == "forty two":
    print("Yes")
# Check if the user's input (converted to lowercase) is equal to "forty-two"
elif user_input.lower() == "forty-two":
    print("Yes")
# If none of the above conditions are met, print "No"
else:
    print("No")
