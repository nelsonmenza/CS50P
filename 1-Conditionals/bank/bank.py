"""
This program evaluates a user-input greeting and assigns a numerical value based on specific conditions. It then prints the assigned value with a "$" symbol.

Usage:
1. Run the program.
2. Enter a greeting when prompted.
3. The program will evaluate the greeting and print the assigned value with a "$" symbol.

Greeting Value Assignments:
- If the greeting contains "hello" (case-insensitive), the value is assigned as $0.
- If the greeting starts with the letter "h" (case-sensitive), the value is assigned as $20.
- If none of the above conditions are met, the value is assigned as $100.

Example:
Greeting: Hello, how are you?
$0
"""


def main():
    # Prompt the user for a greeting
    greeting = input("Greeting: ")
    value = value(greeting)
    print(f"${value}")


def value(greeting):
    # Convert the greeting to lowercase and remove leading/trailing spaces
    greeting = greeting.lower().strip()
    # Check if the greeting contains "hello"
    if "hello" in greeting:
        return 0
    # Check if the greeting contains "h"
    elif greeting[0] == "h":
        return 20
    # If none of the above conditions are met, print "$0"
    else:
        return 100


if __name__ == "__main__":
    main()
