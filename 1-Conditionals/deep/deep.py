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
