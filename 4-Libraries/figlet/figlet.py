# Import the sys module to access command-line arguments and system-related functionality.
import sys
# Import the Figlet class from the pyfiglet library.
from pyfiglet import Figlet
import random  # Import the random module to generate random numbers.


def main():
    # Create an instance of the Figlet class to work with ASCII art fonts.
    figlet = Figlet()
    get_font = figlet.getFonts()  # Get the list of available ASCII art fonts.
    # Get the number of command-line arguments passed to the script.
    len_arg = len(sys.argv)

    # Check if there are command-line arguments and the first argument is not '-f'.
    if len_arg > 1 and sys.argv[1] != "-f":
        # Exit the program with an error message if the usage is invalid.
        sys.exit("Invalid usage")

    # Prompt the user to enter the text to be converted to ASCII art.
    output_text = input("Input: ")

    try:
        # If no additional command-line arguments are provided (default mode).
        if len_arg == 1:
            n = random.randint(1, len(get_font))  # Pick a random font index.
            # Set the font to the randomly selected font.
            figlet.setFont(font=get_font[n])
            # Print the ASCII art text using the chosen font.
            print("Output:\n", figlet.renderText(output_text))

        # If '-f' is provided as the first command-line argument.
        elif len_arg == 3 and sys.argv[1] == "-f":
            # Get the index of the font specified as the second command-line argument.
            n = get_font.index(sys.argv[2])
            # Set the font to the specified font.
            figlet.setFont(font=get_font[n])
            # Print the ASCII art text using the chosen font.
            print("Output:\n", figlet.renderText(output_text))

    except ValueError:
        # Exit the program with an error message if there is an issue with the command-line arguments.
        sys.exit("Invalid usage")


main()  # Call the main function to start the ASCII art generation process.
