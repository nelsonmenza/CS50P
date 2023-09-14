def main():
    # Prompt the user to enter the fuel fraction and calculate the fuel percentage.
    while True:
        try:
            fraction = input("Fraction:")
            # Call the convert function to get the fuel percentage.
            percentage = convert(fraction)
            if percentage is not None:
                break
        except ValueError:
            pass
    # Call the gauge function to determine the fuel status.
    result = gauge(percentage)
    if result == "E" or result == "F":
        print(result)  # Print "E" or "F" if fuel status is empty or full.
    else:
        print(f"{result:.0f}%")  # Print the rounded fuel percentage.


def convert(fraction):
    try:
        # Split the fraction into two parts using the "/" separator.
        a, b = fraction.split("/")
        if a == 0:
            return 0  # Return 0 if the numerator is 0.
        # Calculate the fuel percentage.
        percentage = (int(a) / int(b)) * 100
        if percentage > 100:
            # Return None if the calculated percentage is greater than 100.
            return None
        return percentage  # Return the calculated fuel percentage.
    except (ValueError, ZeroDivisionError):
        # If the input is not a valid fraction or there is a division by zero, ignore the exception.
        pass


def gauge(percentage):
    # If the fuel percentage is less than or equal to 1, return "E" (Empty).
    if percentage <= 1:
        return "E"
    # If the fuel percentage is between 99 and 100 (inclusive), return "F" (Full).
    elif 99 <= percentage <= 100:
        return "F"
    # If the fuel percentage is greater than 100, ask the user for a new fraction.
    elif percentage > 100:
        return -1

    # Return the calculated fuel percentage with a rounded value (no decimal places).
    return percentage


if __name__ == "__main__":
    main()  # Call the main function to start the program.
