import random  # Import the random module for generating random numbers.
import sys  # Import the sys module for system-related functionality.


def main():
    while True:
        try:
            # Prompt the user to input the desired level.
            level = int(input("Level: "))
            # Call the guess function to start the guessing game.
            guess_n = guess(level)
        except ValueError:
            # Ignore ValueError (non-integer input) and continue the loop.
            pass


def guess(level):
    # Generate a random number within the specified level.
    n = random.randint(1, level)
    while True:
        try:
            # Prompt the user to input their guess.
            guess = int(input("Guess: "))
            if guess > n:
                # Print "Too large!" if the guess is greater than the target number.
                print("Too large!")
            elif guess < n:
                # Print "Too small!" if the guess is smaller than the target number.
                print("Too small!")
            else:
                # Exit the program with a message when the correct guess is made.
                sys.exit("Just right!")
        except (ValueError, EOFError):
            # Ignore ValueError (non-integer input) and continue the loop.
            pass


main()  # Call the main function to start the guessing game.
