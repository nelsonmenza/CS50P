# Import the emojize function from the emoji library.
from emoji import emojize

# Prompt the user to enter a string containing emoji shortcuts or plain text with emoji shortcuts.
emojis = input("Input: ")

# Call the emojize function to replace emoji shortcuts in the input string with their corresponding Unicode emojis.
# For example, ":smile:" will be replaced with the 😄 emoji and ":wave:" with the 👋 emoji.
updated_string = emojize(emojis)

# Print the updated string with Unicode emojis to the console.
print(updated_string)
