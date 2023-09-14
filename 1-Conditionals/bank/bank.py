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
