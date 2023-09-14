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
