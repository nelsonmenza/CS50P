import random
import sys


def main():
    # Call get_level to get the desired game level from the user.
    level = get_level()

    # Initialize round and score variables.
    round = 1
    score = 0

    # Iterate through 10 rounds of the game.
    while round < 11:
        # Generate random integers based on the level.
        x, y = generate_integer(level)
        result = rounds(x, y)  # Execute a round of the game.
        if result == True:
            score += 1  # Increase score if the user's answer is correct.
        round += 1  # Move to the next round.

    # Print the final score.
    print(f"Score: {score}")


def get_level():
    # Loop forever to get a valid game level from the user.
    while True:
        try:
            level = int(input("Level: "))  # Prompt for the game level.
        except (ValueError, UnboundLocalError):
            pass  # Ignore errors and continue the loop.
        else:
            # Check if the entered level is between 1 and 3.
            if level > 0 and level < 4:
                return level  # Return the valid game level.
            else:
                pass  # Continue the loop if the level is invalid.


def generate_integer(level):
    # Generate random integers based on the selected game level.
    if level == 1:
        x = random.randint(0, 9)
        y = random.randint(0, 9)
        return x, y
    elif level == 2:
        x = random.randint(10, 99)
        y = random.randint(10, 99)
        return x, y
    elif level == 3:
        x = random.randint(100, 999)
        y = random.randint(100, 999)
        return x, y


def rounds(x, y):
    tries = 0
    while tries < 3:
        try:
            result = int(input(f"{x} + {y} = "))  # Prompt user for an answer.
            if result == x + y and tries != 0:
                return False
            elif result == x + y:
                return True
            else:
                print("EEE")  # Print an error message for incorrect answers.
                tries += 1  # Increment the number of tries.
        except ValueError:
            tries += 1  # Increment the number of tries for non-integer input.
            print("EEE")  # Print an error message for non-integer input.
    print(f"{x} + {y} = {x+y}")  # Print the correct answer.
    return False


if __name__ == "__main__":
    main()  # Call the main function to start the game.
